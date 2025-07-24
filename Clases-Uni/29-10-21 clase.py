# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:24:45 2021

@author: BrandonDLC
"""

import numpy

#Generar un vector de n elementos con ceros por default
mi_vector = numpy.zeros(5)
vector_unitario = numpy.ones(5, dtype = int)
vector = numpy.empty(5)

mi_vector2 = numpy.array([1, 14, 17, 8, 2, 4, 89, 44, 53, 99])

pos = 5

print(mi_vector2[pos] + mi_vector2[pos-1])