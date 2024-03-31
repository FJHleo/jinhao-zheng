from math import exp
import numpy as np
import time

time_start = time.time()


def f(x):
    return exp(x)


def MonteCarlo(Num):
    x = np.arange(0, 1, 1 / Num)
    s = 0
    for ii in range(Num):
        s += f(x[ii])
    s /= Num
    return s


def PrintSolution():
    left = 0
    right = 1
    N = 10
    trueIntegral = exp(1) - 1
    for _ in range(9):
        answer = MonteCarlo(N)
        # print(trueIntegral)
        # print(answer)
        print("N=", N, "\tError=", trueIntegral - answer)
        N *= 10


PrintSolution()

time_end = time.time()
time_sum = time_end - time_start
print(time_sum)
