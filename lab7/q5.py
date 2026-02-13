import numpy as np


A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)


print("Addition (A + B):\n", A + B)

print("Multiplication (A dot B):\n", np.dot(A, B))

print("Transpose of A:\n", A.T)
