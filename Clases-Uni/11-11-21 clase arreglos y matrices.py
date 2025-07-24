# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:32:41 2021

@author: BrandonDLC
"""

#En Python, C, C++, la indexado comienza a partir de o

mi_cadenaC = "hola como estas" #puede ser visto como un vector o arreglo de una dimension

caracter1 = mi_cadenaC[3]
caracter2 = mi_cadenaC[0:3]

#1 2 3
#4 5 6
#7 8 9

for i in range(3):
    for j in range(3):
        if matriz[i][j] == 6:
            x = i
            y = j

matriz = numpy.where(matriz[:,:] == 6)

#%%

#importamos la biblioteca y la apodamos np
import numpy as np

#crear arreglos (vectores 1D | matrice 2D) de forma manual

vector = np.array([1, 2, 3, 4]) #Arreglo de 1 dimension (vector)

resultadov = vector[1] + vector[2]

matriz = np.array([[1, 2], [3, 4]]) #arreglo de 2 dimensiones (matriz)

resultadom = matriz[1][0] + matriz[0][1]

matriz3 = np.array([[[1, 2], [3, 4], [5, 6], [7,8]]]) #arreglo de 3 dimensiones (matriz)

#Estamos definiendo el tipo de dato al momendo de crear el arreglo
vector = np.array([1, 2, 3, 4], dtaye = float)

vec1 = np.arange(10) #arreglo auto de 10 posiciones (del 0-9)
vec1 = np.arange(2, 10, dtype = float) #arreglo del 2-9
vec1 = np.arange(2, 3, 0.1) #arreglo del 2 al 2.9 en incrementos de 0.1

vec1 = np.linspace(1., 4., 6) #Se dividen en valores iguales las celdas del medio

matriz_identidad = np.eye(3)
matriz_identidad = np.eye(3, 5)

vec = np.zeros(5)
vec0 = np.zeros((2, 3))

vec1 = np.ones(5)
mat1 = np.ones((2, 3))

vec_vacio = np.empty(5)
mat_vacio = np.empty((2, 3))

#%%

ejemplo1 = np.array([1, 2, 3, 4, 5, 6])

#siempre debemos hacer una copia para no afectar la matriz o arrieglo primario
ejemplo2 = ejemplo1[:2].copy()
.ejemplo2 += 1

print("ejemplo1 = ", ejemplo1, "; ejemplo 2 = ", ejemplo2)

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([7, 8, 9, 10, 11, 12])
c = np.vstack((a, b))
c = np.hstack((a, b))

x = np.arange(6)
x = np.reshape(x, (3, 2))

y = np.array ([[1, 2], [3, 4]])
z = y.flatten() 




