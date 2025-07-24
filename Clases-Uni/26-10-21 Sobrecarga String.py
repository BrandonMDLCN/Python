# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:03:24 2021

@author: BrandonDLC
"""

class mi_clase:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    #def muestra_datos(self):
     #   print(f'{self.x}, {self.y}, {self.y}')
        
    def __str__(self):
        return f'El valor de x: {self.x}, El valor de Y: {self.y}, El valor de Z: {self.z}'
    
obj1 = mi_clase(1, 2, 3)

print(obj1)