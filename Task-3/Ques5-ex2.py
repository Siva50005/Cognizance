import numpy as np 

# Ex-2 Multiplication of two matrices

mat1 = np.array([[4, 5], [-1, 19], [12, -2]])
mat2 = np.array([[2, 3, 10], [7, -3, 17]])

print("Matrix 1: ")
print(mat1)

print("Matrix 2: ")
print(mat2)

print("Multiplication of matrix 1 and matrix 2: ")
print(np.matmul(mat1, mat2))