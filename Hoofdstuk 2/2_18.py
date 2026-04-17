import numpy as np

matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[4, 3],
                    [2, 1]])

# arrays optellen
print(matrix1 + matrix2)
# [[5 5]
#  [5 5]]

# elementgewijze vermenigvuldiging
print(matrix1 * matrix2)
# [[ 4  6]
#  [ 6  4]]

# matrixvermenigvuldiging
print(matrix1.dot(matrix2))
# [[ 8  5]
#  [20 13]]