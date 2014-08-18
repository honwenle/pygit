#List Comprehensions & Generator
#[expression for for if]
print [x * x for x in range(1, 11) if x % 2 == 0]

import os
print [d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

#(expression for for if)
print (x * x for x in range(10))
# .next()
# for x in g

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
g = fab(6)