from math import exp
import time

time_start = time.time()


def f(x):
    return exp(x)


def Gauss3h_2(left, right, steps):
    result = 0
    step = (right - left) / steps
    i = 0
    for _ in range(steps):
        result += (
            (
                5 * f(((2 * i + 1) * step / 2) - (0.5 * step * ((3 / 5) ** (1 / 2))))
                + 8 * f(((2 * i + 1) * step / 2))
                + 5 * f(((2 * i + 1) * step / 2) - (0.5 * step * ((3 / 5) ** (1 / 2))))
            )
            * step
            / 18
        )
        i += 1
    return result


def Gauss3h(left, right, steps):
    result = 0
    step = (right - left) / steps
    i = 0
    for _ in range(steps):
        result += (
            (
                5 * f(((2 * i + 1) * step / 2) - (0.5 * step * ((3 / 5) ** (1 / 2))))
                + 8 * f(((2 * i + 1) * step / 2))
                + 5 * f(((2 * i + 1) * step / 2) - (0.5 * step * ((3 / 5) ** (1 / 2))))
            )
            * step
            / 18
        )
        i += 1
    return result, step


def PrintSolution():
    left = 0
    right = 1
    number_of_steps = 10
    number_of_steps2 = number_of_steps * 2
    step_h = 0
    step_2h = 0
    error = 1000
    while abs(error) > 10 ** (-8):
        integralh, step_h = Gauss3h(left, right, number_of_steps)
        integralh_2, step_2h = Gauss3h(left, right, number_of_steps2)
        error = (integralh - integralh_2) * (1 / (2**7 - 1))
        number_of_steps = number_of_steps2
        number_of_steps2 = number_of_steps2 * 2
        print("step width = ", step_2h, "error = ", abs(error))


PrintSolution()
