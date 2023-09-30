# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:48:55 2021

@author: BrandonDLC
"""

#SOBRECARGA DE OPERADORES

#AQUI NO SE VA A UTILIZAR LA SOBRECARGA

class vector:
    
    def __init__(self, v1, v2):
        self.pos1 = v1
        self.pos2 = v2
        
v_a = vector(8, 9)
v_b = vector(14, 27)

#SUMA
v1 = v_a.pos1 + v_b.pos1
v2 = v_a.pos2 + v_b.pos2
resultado = vector(v1, v2)
print('Suma = (%f, %f)' % (resultado.pos1, resultado.pos2))

#RESTA
v1 = v_a.pos1 - v_b.pos1
v2 = v_a.pos2 - v_b.pos2
resultado = vector(v1, v2)
print('Resta = (%f, %f)' % (resultado.pos1, resultado.pos2))

#MULTIPICAR
esc = 7.891
v1 = v_a.pos1 * esc
v2 = v_a.pos2 * esc
resultado = vector(v1, v2)
print('Multiplicacion = (%f, %f)' %(resultado.pos1, resultado.pos2))



#%%

#operacion suma: __add__ = +

class vector:
    
    def __init__(self, v1, v2):
        self.pos1 = v1
        self.pos2 = v2
        
    def __add__(self, x): #Suma
        return vector(self.pos1 + x.pos1, self.pos2 + x.pos2)
    
    def __sub__(self, x):  #Resta
        return vector(self.pos1 - x.pos1, self.pos2 - x.pos2)
    
    def __mul__(self, esc): #Multiplicación
        return vector(self.pos1 * esc, self.pos2 * esc)

    def __truediv__(self, esc): #Divición
        float_esc = float(esc)
        return vector(self.pos1 / float_esc, self.pos2 / float_esc)
    
    
v_a = vector(8, 9)
v_b = vector(14, 27)
        
suma = v_a + v_b #cada vez se crea un nuevo objeto/instancia
resta = v_a - v_b
multi = v_a * 7.891
div = v_a / 17

print(suma.pos1, suma.pos2)
print(resta.pos1, resta.pos2)
print(multi.pos1, multi.pos2)
print(div.pos1, div.pos2)










