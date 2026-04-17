import numpy as np

matrix = np.array([[1, 5, 6],
                   [4, 7, 2],
                   [3, 1, 9]])

# maximum van de volledige array
print(matrix.max())          # 9

# maximum per rij
print(matrix.max(axis=1))    # [6 7 9]

# minimum per kolom
print(matrix.min(axis=0))    # [1 1 2]

# som van alle elementen
print(matrix.sum())          # 38

# cumulatieve som per rij
print(matrix.cumsum(axis=1))    # [[ 1  6 12]
                                #  [ 4 11 13]
                                #  [ 3  4 13]]