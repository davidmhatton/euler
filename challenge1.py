# !/usr/bin/python
__author__ = 'dhatton'

multiples = []

for x in range(0, 1000):
    if (x % 3) == 0 or (x % 5) == 0:
        multiples.append(x)

print sum(multiples)
