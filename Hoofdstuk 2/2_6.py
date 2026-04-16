import numpy as np

matrix_34 = np.array([[1, 2, 3, 4], [5, 2, 4, 2], [1, 2, 0, 1]])
matrix_62 = matrix_34.reshape(6, 2)

print(matrix_34)
print(matrix_62)