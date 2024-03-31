from math import exp


def f(x):
    return exp(-x)


def diffe(x, steps):
    h = 1 / steps
    result = (
        -f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)
    ) / (12 * h**2)
    return result


def PrintSolution():
    x = 0
    N = 10
    h = 1 / N
    trueIntegral = 1
    for _ in range(9):
        answer = diffe(x, N)
        print("N=", N, "\th=", h, "\tError=", trueIntegral - answer)
        N *= 10
        h /= 10


PrintSolution()
