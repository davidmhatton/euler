# !/usr/bin/python


def is_palendromic(number):
    string = str(number)
    size = len(number)
    for x in range(0, size):
        if string[x] == string[size - x]:
            return False
    return True

large1 = 999
large2 = 999


def runner(number1, number2, cycle):
    for a in range(number1, number1 - cycle, -1):
        for b in range(number2, number2 - cycle, -1):
            print str(a) + ', ' + str(b)

runner(40, 40, 10)
