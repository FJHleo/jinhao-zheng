from math import exp


def f(x):
    return exp(-x)


def diffe2(x, steps):
    h = 1 / steps
    result = (f(x + 0.5 * h) - f(x - 0.5 * h)) / h
    return result


def PrintSolution():
    x = 0
    N = 10
    h = 1 / N
    trueDiffe = -1
    for _ in range(9):
        answer = diffe2(x, N)
        print("N=", N, "\th=", h, "\tError=", trueDiffe - answer)
        N *= 10
        h /= 10


PrintSolution()
