
from functional_util import then, keep, remove, windowed, change
import math


x1 = range(1,20)

x2 = range(1,20) \
     | then | keep(lambda x : x % 3 == 0 or x % 5 == 0)

x3 = range(1,20) \
     | then | keep(lambda x : x % 3 == 0 or x % 5 == 0) \
     | then | change(lambda x : x * x)

x4 = range(1,20) \
     | then | keep(lambda x : x % 3 == 0 or x % 5 == 0) \
     | then | change(lambda x : x * x) \
     | then | sum

print(x1)
print(x2)
print(x3)
print(x4)
