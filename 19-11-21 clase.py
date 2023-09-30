# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:10:05 2021

@author: BrandonDLC
"""

import numpy as np
from matplotlib import pyplot as plt

datos_string = np.loadtxt("C:\\Users\\BrandonDLC\\Downloads\\3dic2016.txt", delimiter = "\n", skiprows = 0, dtype = "str")

puntos = np.char.find(datos_string, "PC05")

puntos = np.where(puntos > -1)

puntos = int(puntos[0])

datos_string2 = datos_string[puntos]

datos_string2 = datos_string2.replace("PC05", "")

datos_string2 = datos_string2[1:]

datos_string2 = datos_string2.split(sep = " ", maxsplit = 3)

datos_string2 = np.asarray(datos_string2, dtype = float)










