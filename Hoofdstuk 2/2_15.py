import numpy as np

matrix = np.array([1, 2, 5, 3]) 
  
# 1 optellen bij elk element
matrix_som = matrix+1
  
# 3 aftrekken van elk element
matrix_verschil = matrix-3
  
# elk element vemenigvuldigen met 10
matrix_vermenigvuldiging = matrix*10
  
# het kwadraat nemen van elk element
matrix_macht = matrix**2
  
# bestaande array aanpassen
matrix *= 2

print(matrix_som)
print(matrix_verschil)
print(matrix_vermenigvuldiging)
print(matrix_macht)
print(matrix)