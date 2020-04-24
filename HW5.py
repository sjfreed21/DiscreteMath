# Sam Freed

from z3 import *

def check_validity(sentence):
    s = Solver()
    s.add(Not(sentence))
    result = s.check()
    if result == sat:
        print('Invalid.')
    elif result == unsat:
        print('Valid.')
    else:
        print('Unable to solve.')

x = Int("x")
y = Int("y")
z = Int("z")

S1 = ForAll([x], Exists([y], And(x <= y, ForAll([z], Or(x >= z, z >= y)))))

check_validity(S1)