## Samuel Freed
## Solution: 749669676277

from sympy import isprime
from mpmath import mp

decimalPlaces = 100
with mp.workdps(decimalPlaces):
    estring = str(mp.e).replace('.','')

for i in range(0,(decimalPlaces-12)):
    t = int(estring[i:i+12])
    if(isprime(t)):
        print(t, 'at i =', i)
        break
