# Samuel Freed
# Solution: Both V and W are guilty since z3 outputs true for both.

from z3 import *

def block_model(s):
    m = s.model()
    return a != m[a]

def print_model(s):
    m = s.model()
    print(v, '=', m[v], ',', w, '=', m[w])

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

s = Solver()
a,b,c,d,e,f,g,h = [Bool(s) for s in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
v = Bool('v')
w = Bool('w')

s.add(a == a)                               # A asserts A is a knight
s.add(c == Not(a))                          # C asserts A is a knave
s.add(d == Not(b))                          # D asserts B is a knave
s.add(e == And(c, d))                       # E asserts C and D are knights
s.add(f == Or(a, b))                        # F asserts A or B are knaves
s.add(g == (e == f))                        # G asserts E and F are the same
s.add(h == And(g == h, Not(And(v, w))))     # H asserts G and H are the same and V or W are guilty

solve_and_print(s)