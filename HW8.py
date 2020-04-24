# Sam Freed
# Indices Chosen: [0, 2, 9]

from z3 import *

def set_cover(Ca):
    n = max([max(subs) for subs in Ca]) + 1
    x = [Bool('s%s' % i) for i in range(n)]
    o = Optimize()
    o.minimize(Sum([If(v,1,0) for v in x]))
    o.add([Or([x[i] for i in subs]) for subs in Ca])
    if o.check() == sat:
        m = o.model()
        return [i for i in range(n) if is_true(m[x[i]])]
    else:
        return None

if __name__ == '__main__':
    Ca = [{0,10}, {0,1,4}, {1,2,4,5,6,7}, {0,1,3,5,9}, {0,3}, {2,6,8,11}, {2,7,8,10}, {3,9}]
    print(set_cover(Ca))
