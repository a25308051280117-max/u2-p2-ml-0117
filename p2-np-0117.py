import numpy as np
# Matias Lopez NC 0117
# Ejemplos de Numpy  Numerical Python
print("-- Espaciado linealmente en array--0117")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("--Matriz identidad en 2D array--0117")
matrix=np.eye(3)
print(matrix)
print("--Genera numeros al azar(aleatoriamente) en 2D array--0117")
numale=np.random.random((3,4))# genera 12 numeros alateorios
print(numale)
print("generar 9 numeros alateorios entre 0 y 1")
numale=np.random.random((3,3))# genera 12 numeros alateorios
print(numale)
#como generar 9 numeros alatorios comprendidos entre 1 y20
# con numpy en un arreglo de 3 por 3
print("generar 9 numeros alateorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Matias Lpoez NC 0117")