def eno(a, b, x0, y0, n):
    a = a
    b = b
    x = x0
    y = y0

    result = []
    for i in range(n):
        x = 1 - a * x ** 2 - b * y
        y = x
        result.append(y)
    return result
