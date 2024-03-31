import math
import numpy as np
import matplotlib.pyplot as plt

h = 1 / 10 ** (4)


def f(theta):
    return 90 * (np.cos(theta) + ((2.5**2) - (np.sin(theta)) ** 2) ** 0.5)


def diffe2(theta):
    s = (f(theta + h) - 2 * f(theta) + f(theta - h)) / (h**2)
    return s


def accele():
    theta = np.linspace(0, math.pi, 36)
    answer = diffe2(theta) * (2 * math.pi * 5000 / 60) ** 2
    for i in range(36):
        print("theta=", theta[i], "\tacceleration", answer[i])
    plt.plot(theta, answer)
    plt.show()


accele()
