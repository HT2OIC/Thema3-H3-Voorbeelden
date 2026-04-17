import numpy as np

matrix = np.array([[ 1,  4,  2],
                   [ 3,  4,  6],
                   [ 0, -1,  5]])

# alle elementen samen sorteren
print(np.sort(matrix, axis=None))
# [-1  0  1  2  3  4  4  5  6]

# elke rij apart sorteren
print(np.sort(matrix, axis=1))
# [[ 1  2  4]
#  [ 3  4  6]
#  [-1  0  5]]

# elke kolom apart sorteren
print(np.sort(matrix, axis=0, kind='mergesort'))
# [[ 0 -1  2]
#  [ 1  4  5]
#  [ 3  4  6]]