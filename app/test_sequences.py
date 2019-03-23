import numpy as np


def eno(a, b, x0, y0, n):
    x = x0
    y = y0

    result = []
    for i in range(n):
        x = 1 - a * x ** 2 - b * y
        y = x
        result.append(y)
    return result


def linear(a, b, x0, n):
    result = []
    x = x0
    for i in range(n):
        x = a + b * x
        result.append(x)
    return result


def logistic(x0, lamb, n):
    x = x0
    result = []
    for i in range(n):
        x = 1 - lamb * x * x
        result.append(x)
    return result
