from functools import partial

def pipe(start,*fs):
    temp = start
    for f in fs:
        temp = f(temp)
    return temp

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

then = Infix(lambda x,f: f(x))

def keep(f):
    return lambda xs: [x for x in xs if f(x)]

def remove(f):
    return lambda xs: [x for x in xs if not f(x)]

def change(f):
    return lambda xs: [f(x) for x in xs]

def forall(f):
    return lambda xs: all(f(x) for x in xs)

def AllPairs(xs,ys):
    return [(x,y) for x in xs for y in ys]

def windowed(n):
    return lambda xs: [
        xs[i:][0:n]
        for i in range(0,len(xs))
        if len(xs[i:][0:n]) == n
    ]

def reduce(f):
    def hidden(x0):
        def hidden2(xs):
            temp = x0
            for x in xs:
                temp = f(x,temp)
            return temp
        return hidden2
    return hidden
    

def accumulate(f):
    def hidden(x0):
        def hidden2(xs):
            temp = x0
            result = []
            result.append(temp)
            for x in xs:
                temp = f(x,temp)
                result.append(temp)
            return result
        return hidden2
    return hidden

def accumulate_with(fs):
    def inner(x0):
        temp = x0
        result = []
        result.append(temp)
        for f in fs:
            temp = f(temp)
            result.append(temp)
        return result
    return inner