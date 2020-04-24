## Samuel Freed
## When k = 4, there are 84 solutions, confirming our previous calculations.

from typing import List, Set

Graph = List[Set[int]]

from z3 import *

def Chromatic(G: Graph , k:int):
    """ Finds k-coloring  of G."""
    n = len(G)
    v = [Int('v%i' % i) for i in range(n)]
    s = Solver()
    s.add([And(x>=0, x<k) for x in v])
    for i in range(n):
        s.add([v[i] != v[j] for j in G[i]])
    cnt = 0
    while s.check() == sat:
        cnt += 1
        m = s.model()
        print(m)
        s.add(Not(And([v[i] == m[v[i]] for i in range (n)])))

    return cnt

g = [
    {1,2},
    {0,3},
    {0,3},
    {1,2}
]

print(Chromatic(g,4))