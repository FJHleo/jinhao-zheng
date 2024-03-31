import numpy as np


def gaussian(A, b):
    n = len(b)
    for k in range(0, n - 1):  # 每一个主元素所在行
        for i in range(k + 1, n):  # 每一个主元素所在列，即主元素下面一系列值
            if A[i, k] != 0.0:
                lam = A[i, k] / A[k, k]
                A[i, k + 1 : n] = A[i, k + 1 : n] - lam * A[k, k + 1 : n]
                b[i] = b[i] - lam * b[k]
    for i in range(n - 1, -1, -1):
        b[i] = (b[i] - np.dot(A[i, i + 1 : n], b[i + 1 : n])) / A[i, i]
    return b


A = np.array(
    [
        [0.0, 0.0, 2.0, 1.0, 2.0],
        [0.0, 1.0, 0.0, 2.0, -1.0],
        [1.0, 2.0, 0.0, -2.0, 0.0],
        [0.0, 0.0, 0.0, -1.0, 1.0],
        [0.0, 1.0, -1.0, 1.0, -1.0],
    ]
)

# Row 1, 3 vectors in the matrix are swapped, so that the matrix satisfies the conditions of the Gaussian elimination method
tmpA = np.copy(A[0])
A[0] = A[2]
A[2] = tmpA


b1 = np.array([1.0, 1.0, -4.0, -2.0, -1.0])

# Row 1, 3 vectors in the matrix are swapped, so that the matrix satisfies the conditions of the Gaussian elimination method
tmpb = np.copy(b1[0])
b1[0] = b1[2]
b1[2] = tmpb
print(b1)


X = gaussian(A, b1)

# X = np.linalg.solve(A, b1)   # Verification results

print("X=", X)
