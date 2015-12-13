# !/usr/bin/python
limit = 4000000
fibs = []


def fib(n):
    a, b = 1, 2
    for i in range(n-1):
        a, b = b, a + b
    return a

# for x in range(1, 100):
#     print 'fib ' + str(x) + ': ' + str(fib(x))


k = 1
y = 1
while y < limit:
    y = fib(k)
    if y < limit and y % 2 == 0:
        fibs.append(y)
        print 'k = ' + str(k) + ', y = ' + str(y)
    k += 1

print sum(fibs)
