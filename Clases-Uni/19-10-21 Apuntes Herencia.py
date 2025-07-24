# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:02:25 2021

@author: BrandonDLC
"""

#UNIDAD 3. HERENCIA
#apunte
class mi_clase:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def mi_metodo(self):
        print('Hola como estas?')
        
obj1 = mi_clase(x, x, z)
obj2 = mi_clase(x, x, z)

class clase_base:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def mi_metodo(self):
        print('Hola como estas?')

class clase_sec(clase_base):
    
    def met_dos(self):
        print('x+X = self.x, Y = self.y, Z = self.z')
        
obj1 = clase_sec()

#%%
#HERENCIA SIMPLE

class claseBase:
    .....
    .....
    .....
class claseSec(claseBase):
    .....
    .....
    .....
class claseSec2(claseBase):
    .....
    .....
    .....
class claseSec3(claseBase):
    .....
    .....
    .....











