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


A = np.array([[6.0, -4.0, 1.0], [-4.0, 6.0, -4.0], [1.0, -4.0, 6.0]])
b1 = np.array([-14.0, 36.0, 6.0])
b2 = np.array([22.0, -18.0, 7.0])
X1 = gaussian(A, b1)
X2 = gaussian(A, b2)
print("X1=", X1, "X2=", X2)
