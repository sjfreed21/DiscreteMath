# Sam Freed
# Permutation for N = 17:
# 16 9 7 2 14 11 5 4 12 13 3 6 10 15 1 8 17

from z3 import *
import sys
import math

def block_model(s):
    m = s.model()
    return Or([v != m[v] for v in x])

def print_model(s):
    m = s.model()
    print(' '.join([str(m[v]) for v in x]))

def solve_and_print(s):
    result = s.check()
    if result == sat:
        print_model(s)
        if s.check(block_model(s)) == unsat:
            print('unique solution')
        else:
            print('solution not unique')
    elif result == unsat:
        print('unsatisfiable constraints')
    else:
        print('unable to solve')

if len(sys.argv) > 2:
    raise SystemExit("There should be at most one argument!")
elif len(sys.argv) == 2:
    try:
        N = int(sys.argv[1])
    except:
        raise SystemExit("Input for N must be an integer.")
    if N < 0:
        raise SystemExit("N must be greater than 0.")
else:
    N = 15

x = Ints(['x_%s' % (i+1) for i in range(N)])

squares = []

for x in range(1,2*N+2):
    root = math.sqrt(x)
    if int(root + 0.5) ** 2 == x:
        squares.append(x)

print(squares)

areSquares = [Or([x[k] + x[k+1] == s for s in squares]) for k in range(N-1)]
Bounds = [And(0 < v, v <= N) for v in x]
symmBreak = x[0] < x[N-1]

s = Solver()
s.add(Distinct(x))
s.add(Bounds)
s.add(areSquares)
s.add(symmBreak)

solve_and_print(s)