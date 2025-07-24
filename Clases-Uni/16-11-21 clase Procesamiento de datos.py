# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:24:24 2021

@author: BrandonDLC
"""

#PROCESAMIENTO DE DATOS: EXTRACCION DE INFORMACION DE INTERES DE UN GRUPO DE DATOS


#FORMA ESTATICA

#FORMA DINAMICA

import numpy as np

from matplotlib import pyplot as plt
#vector = np.array([1, 2, 3, 4])
#vector_c = np.empty(15)

#LA SIGUIENTE LINEA SE UTILIZA PARA LEER INFORMACION DE UN ARCHIVO
#"delimiter" para ignorar los saltos de palabras en este caso son espacios
#"usecols" sirve para brincarnos las columnas (se empiezza por el numero 0)
#"skiprows" sirve para saltarse una linea (en numero de lineas en enteros)
datos = np.loadtxt("C:\\Users\\BrandonDLC\\Downloads\\3dic2016.txt", delimiter = " ", skiprows = 1, usecols =(1, 2, 3, 4), dtype = float)