import numpy as np


A = np.array([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0], [3.0, 4.0, 5.0]])
B = np.array([[2.11, -0.80, 1.72], [-1.84, 3.03, 1.29], [-1.57, 5.25, 4.30]])
C = np.array([[2.0, -1.0, 0], [-1.0, 2.0, -1.0], [0.0, -1.0, 2.0]])
D = np.array([[4.0, 3.0, -1.0], [7.0, -2.0, 3.0], [5.0, -18.0, 13.0]])


list = [A, B, C, D]


for i in range(4):
    r = np.linalg.matrix_rank(list[i])
    if r == 3:
        print(i + 1, ":", list[i], "This matrix is linearly uncorrelated")
    else:
        print(i + 1, ":", list[i], "This matrix is linearly correlated")
