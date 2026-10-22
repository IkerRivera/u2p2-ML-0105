import numpy as np
# Iker Montoya NC 0105
#Ejemplos numpy numerical Python 
print("-- Espaciado linealmente en array  -- 0105")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- matriz identidad  en 2D array  -- 0105")
matrix=np.eye(3)
print(matrix)
print("-- genero numero al azar(aleatorios) en 2D array -- 0105")
numale=np.random.random((3,4)) # genera 12 numeros 
print(numale)
print("generar numeros aleatorios entre 0 y 1 ")
numale=np.random.random((3,3)) # genera 9 numeros aleatorios 
print(numale)
#como generar 9 numeros aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3 por 3 
print("generar 9 numeros aleatorios entre 1 y 20 ")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Iker Montoya NC = 0105")