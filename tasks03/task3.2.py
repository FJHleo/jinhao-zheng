from math import exp


def f(x):
    return exp(x)


def diffe(x, steps):
    h = 1 / steps
    result = (-1 / 3) * (f(x + h / 2) - f(x - h / 2)) / h + (4 / 3) * (
        f(x + h) - f(x - h)
    ) / (2 * h)
    return result, h


def diffe_2(x, steps):
    h = 1 / steps
    result = (-1 / 3) * (f(x + h / 2) - f(x - h / 2)) / h + (4 / 3) * (
        f(x + h) - f(x - h)
    ) / (2 * h)
    return result, h


def PrintSolution():
    x = 0
    number_of_steps = 10
    number_of_steps2 = number_of_steps * 2
    step_h = 0
    step_2h = 0
    error = 1000
    count = 0
    while abs(error) > 10 ** (-8):
        differential, step_h = diffe(x, number_of_steps)
        differential_2, step_2h = diffe(x, number_of_steps2)
        error = (differential - differential_2) * (1 / (2**4 - 1))
        number_of_steps = number_of_steps2
        number_of_steps2 = number_of_steps2 * 2
        count += 1
        print("step width = ", step_2h, "\terror = ", abs(error), "\tcount = ", count)


PrintSolution()
