from functools import partial
import math


def pipe(start, *fs):
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


then = Infix(lambda x, f: f(x))


def keep(f):
    def hidden(xs):
        temp = []
        for x in xs:
            if f(x):
                temp.append(x)

        return temp

    return hidden


def remove(f):
    return keep(lambda x: not (f(x)))


def forall(f):
    def hidden(xs):
        for x in xs:
            if not (f(x)):
                return False

        return True

    return hidden


def change(f):
    def hidden(xs):
        temp = []
        for x in xs:
            temp.append(f(x))

        return temp

    return hidden


def IsPrime(x):
    if x in (2, 3, 5, 7):
        return True
    elif x in (1, 4, 6, 8, 9):
        return False
    elif x % 2 == 0 or x < 0:
        return False
    else:
        sqrt_x = int(math.sqrt(x)) + 1
        return range(3, sqrt_x, 2) \
               | then | forall(lambda y: x % y != 0)


def AllPairs(xs, ys):
    temp = []
    for x in xs:
        for y in ys:
            temp.append((x, y))

    return temp


def windowed(n):
    def hidden(xs):
        result = []
        temp = []
        for x in xs:
            temp.append(x)
            if len(temp) == n:
                result.append(temp)
                temp = temp[1:]

        return result

    return hidden


def reduce(f):
    def hidden(x0):
        def hidden2(xs):
            temp = x0
            for x in xs:
                temp = f(x, temp)
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
                temp = f(x, temp)
                result.append(temp)
            return result

        return hidden2

    return hidden