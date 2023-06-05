from math import pi
def fact(x):
    if x != 1:
        return x*fact(x-1)
    else:
        return 1
def sine(x, e, deg):
    if deg:
        x *= pi/180
    x %= 2*pi
    n = 1
    a_n = (-1) ** (n+1) * x ** (2*n-1) / fact(2 * n - 1)
    seriesSum = a_n
    while abs(a_n) > (10 ** (-e-1)):
        n += 1
        a_n = (-1) ** (n + 1) * x ** (2 * n - 1) / fact(2 * n - 1)
        seriesSum += a_n
    if seriesSum > 1:
        seriesSum = 1
    if seriesSum < -1:
        seriesSum = -1
    return seriesSum
def cosine(x, e, deg):
    if deg:
        return sine(90 - x, e, deg)
    else:
        return sine(pi / 2 - x, e, deg)
def tangent(x, e, deg):
    if deg:
        x *= pi / 180
        deg = False
    if abs((x+pi/2) % pi) < (10**(-e)):
        return "The argument is a pi*k+pi/2 (180k+90 degrees) (where k is an integer) type number - this tan(x) does not exist"
    else:
        return sine(x, e, deg) / cosine(x, e, deg)
def cotangent(x, e, deg):
    if deg:
        x *= pi / 180
        deg = False
    if abs(x % pi) < (10**(-e)):
        return "The argument is a multiple of pi (180 degrees) (or is 0) - this cot(x) does not exist"
    else:
        return cosine(x, e, deg) / sine(x, e, deg)
def secant(x, e, deg):
    if deg:
        x *= pi / 180
        deg = False
    if abs((x + pi / 2) % pi) < (10 ** (-e)):
        return "The argument is a pi*k+pi/2 (180k+90 degrees) (where k is an integer) type number - this sec(x) does not exist"
    else:
        return 1 / cosine(x, e, deg)
def cosecant(x, e, deg):
    if deg:
        x *= pi / 180
        deg = False
    if abs(x % pi) < (10**(-e)):
        return "The argument is a multiple of pi (180 degrees) (or is 0) - this csc(x) does not exist"
    else:
        return 1 / sine(x, e, deg)
