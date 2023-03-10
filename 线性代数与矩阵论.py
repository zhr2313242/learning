import numpy as np

A = np.array([[1, 0], [0, 1]])
B = np.array([[4, 1], [2, 2]])
C = np.dot(A, B)
D = np.linalg.inv(C)

print(C)
print(D)
