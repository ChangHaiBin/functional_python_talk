
from functional_util import pipe

def f1(x): return x + 1
def f2(x): return x + 2
def f3(x): return x + 3

fs = [f1, f2, f3]

pipe(
    100,
    *fs,
    print
)