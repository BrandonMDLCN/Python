# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:53:25 2021

@author: BrandonDLC
"""

import numpy as np
from matplotlib import pyplot as plt

datos = np.loadtxt("C:\\Users\\BrandonDLC\\Downloads\\3dic2016.txt", delimiter = " ", skiprows = 1, usecols =(1, 2, 3, 4), dtype = float)

puntos = np.where((datos[:,3] >= 30) & (datos[:,3] <31))

#asarray para cambiar tipo de dato
puntos = np.asarray(puntos, dtype = int).flatten()

datos2 = datos[puntos]

#codigo para guardar datos, poner al final de la ruta el nombre del archivo a crear
np.savetxt("C:\\Users\\BrandonDLC\\Downloads\\resultados.txt", datos2, delimiter = "\t")

datos2.dtype

datos2.shape

filas = datos2.shape[0]

columnas = datos2.shape[1]

datos2.size

x = datos2[:,2]
y = datos2[:,3]

plt.title("Mediciones con Arduino")
plt.xlabel("Humedad (% Rel) ")
plt.ylabel("Temperatura(*C)")
plt.plot(x, y)

#Guardar el plot
plt.gcf()
plt.savefig("C:\\Users\\BrandonDLC\\Downloads\\mi_grafica.png", dpi = 300, bbox_inches = "tight")
plt.close()

plt.show()

#%%

#CONCATENACION DE MATRICES
c = np.vstack((datos,datos2))

la matriz de strings(str)
la matriz de enteros (str)

matriz_enteros = str(matriz_original) #opcion 1
matriz_enteros = np.asarray(matriz_original, dtype = str) #opcion 2

matriz_final = np.asarray(matriz_strings, dtype = object)
matriz_final = np.asarray(matriz_enteros,dtype = object)

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([])


