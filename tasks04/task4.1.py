from math import exp


def f(x, n):
    return (1 / exp(1)) * (x**n) * (exp(x))


def Gauss3h(left, right, steps, n):
    result = 0
    step = (right - left) / steps
    i = 0
    for _ in range(steps):
        result += (
            (
                5 * f(((2 * i + 1) * step / 2) - (0.5 * step * ((3 / 5) ** (1 / 2))), n)
                + 8 * f(((2 * i + 1) * step / 2), n)
                + 5
                * f(((2 * i + 1) * step / 2) - (0.5 * step * ((3 / 5) ** (1 / 2))), n)
            )
            * step
            / 18
        )
        i += 1
    return result, step


def PrintSolution():
    left = 0
    right = 1
    for n in range(31):
        number_of_steps = 10
        number_of_steps2 = number_of_steps * 2
        step_h = 0
        step_2h = 0
        error = 0
        while abs(error) > 10 ** (-8):
            integralh, step_h = Gauss3h(left, right, number_of_steps, n)
            integralh_2, step_2h = Gauss3h(left, right, number_of_steps2, n)
            error = (integralh - integralh_2) * (1 / (2**7 - 1))
            number_of_steps = number_of_steps2
            number_of_steps2 = number_of_steps2 * 2
        correct_answer, tmp = Gauss3h(left, right, number_of_steps, n)
        iterative_answer = recursion(n)
        error = abs(iterative_answer - correct_answer)
        print(
            "error = ",
            error,
            "correct = ",
            correct_answer,
            "iterative answer = ",
            iterative_answer,
            "n = ",
            n,
        )
        if error >= correct_answer:
            print("!!!ABOBA!!! the error is too high!!!")
            break


def recursion(n):
    I0 = 1 - exp(-1)
    if n == 0:
        return I0
    else:
        return 1 - n * recursion(n - 1)


PrintSolution()
