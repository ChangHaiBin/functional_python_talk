
from functional_util import then, keep, remove, windowed, change, forall, AllPairs, reduce, accumulate
import math

def IsPrime(x):
    if x in (2,3,5,7):
        return True
    elif x in (1,4,6,8,9):
        return False
    elif x % 2 == 0 or x < 0:
        return False
    else:
        sqrt_x = int(math.sqrt(x)) + 1
        return range(3,sqrt_x,2) \
            | then | forall(lambda y : x % y != 0)


def t2(f):
    def hidden(tp):
        (x1,x2) = tp
        return f(x1,x2)
    return hidden
def t3(f):
    def hidden(tp):
        (x1,x2,x3) = tp
        return f(x1,x2,x3)
    return hidden


    
# Question 1
print("Question 01: ", end="")
range(1,1000) \
| then | keep(lambda x : x % 3 == 0 or x % 5 == 0) \
| then | sum \
| then | print

# Question 2
print("Question 02: ", end="")
def next_fib(tp):
    (a,b) = tp
    return (b,a+b)
fib_start = (1,2)
base = \
    range(1,50) \
    | then | accumulate(lambda _, tp: next_fib(tp))(fib_start) \
    | then | change(lambda tp: tp[0])

base \
| then | keep(lambda x : x < 4000000) \
| then | keep(lambda x : x % 2 == 0) \
| then | sum \
| then | print

# Question 3:
# Warning: This is not the general way to solve this kind of problems!
print("Question 03: ", end="")
range(1,780000) \
| then | keep(lambda x : 600851475143 % x == 0) \
| then | keep(IsPrime) \
| then | max \
| then | print

# Question 4:
print("Question 04: ", end="")
def IsPalindrome(x):
    s=str(x)
    return s == s[::-1]
three_digits = range(1,1000)
AllPairs(three_digits,three_digits) \
| then | change(t2(lambda x,y: x * y)) \
| then | keep(IsPalindrome) \
| then | max \
| then | print

# Question 5:
print("Question 05: ", end="")
def gcd(x,y):
    if x > y:
        return gcd(y,x)
    elif x < 0 or y < 0:
        return 0
    elif x == 0:
        return y
    else:
        return gcd(y%x,x)

def lcm(x,y):
    return (x * y) // gcd(x,y)

range(1,21) \
| then | reduce(lcm)(1) \
| then | print

# Question 6:
print("Question 06: ", end="")
sum_of_squares = \
    range(1,101) \
    | then | change(lambda x : x * x) \
    | then | sum
square_of_sums = \
    range(1,101) \
    | then | sum \
    | then | (lambda s: s * s)

print(square_of_sums - sum_of_squares)

# Question 7:
print("Question 07: ", end="")
range(1,500000) \
| then | keep(IsPrime) \
| then | (lambda xs: xs[10000]) \
| then | print

# Question 8:
print("Question 08: ", end="")
def product(xs):
    return reduce(lambda x,y: x*y)(1)(xs)

'''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''.replace('\n','') \
| then | change (int) \
| then | windowed(13) \
| then | change(product) \
| then | max \
| then | print

# Question 9:
print("Question 09: ", end="")
thousands = range(1,1001)
AllPairs(thousands, thousands) \
| then | change(t2(lambda a,b: (a,b,1000 - a - b))) \
| then | keep(t3(lambda a,b,c:a * a + b * b == c * c and  a < b < c)) \
| then | change(t3(lambda a,b,c: a * b * c)) \
| then | print

# Question 10:
# Not the most efficient method.
print("Question 10: ", end="")
range(3,2000000,2) \
| then | keep(IsPrime) \
| then | sum \
| then | (lambda s : s + 2) \
| then | print

