import numpy as np


def gaussian(A, b):
    n = len(b)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if A[i, k] != 0.0:
                lam = A[i, k] / A[k, k]
                A[i, k + 1 : n] = A[i, k + 1 : n] - lam * A[k, k + 1 : n]
                b[i] = b[i] - lam * b[k]
    for i in range(n - 1, -1, -1):
        b[i] = (b[i] - np.dot(A[i, i + 1 : n], b[i + 1 : n])) / A[i, i]
    return b


A = np.array([[2.0, -3.0, -1.0], [3.0, 2.0, -5.0], [2.0, 4.0, 1.0]])
b = np.array([3.0, -9.0, -5.0])
X = gaussian(A, b)
print("X=", X)
