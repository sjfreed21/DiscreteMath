# Samuel Freed
# Solution: a = False
# This means that Alex is a knave and nothing can be determined about his mother.

from z3 import *
s = Solver()
a = Bool('a') # If true, Alex is a knight
m = Bool('m') # If true, Alex's mother is a knight

# in case you forgot my name, look at the first three letters of lines 6-8! funny coincidence :)

# If a is true, then m is true only if a and m are opposites
# If a is false, nothing can be determined about m

s.add(a == Or( And(a,Not(m)), And(m,Not(a)) )) # This is an exclusive or gate

result = s.check()
if result == sat:
    m = s.model()
    print(', '.join([str(a) + ' = ' + str(m[a])]))

elif result == unsat:
    print('unsatisfiable')

else:
    print('unable to solve')