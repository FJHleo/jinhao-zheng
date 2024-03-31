from math import exp


def f(x):
    return exp(-x)


def diffe(x, steps):
    h = 1 / steps
    result = (f(x + h) - f(x)) / h
    return result


def PrintSolution():
    x = 0
    N = 10
    h = 1 / N
    trueDiffe = -1
    for _ in range(9):
        answer = diffe(x, N)
        print("N=", N, "\th=", h, "\tError=", trueDiffe - answer)
        N *= 10
        h /= 10


PrintSolution()
