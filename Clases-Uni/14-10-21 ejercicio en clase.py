# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:44:29 2021

@author: BrandonDLC
"""

class hexaedro:
    
    def __init__(self, arista):
        self.a = arista
    
    def base(self):
        b = self.a * self.a
        print('La base es', b)
        
    def area_lateral(self):
        areal = 4 * self.a
        print('El area lateral es', areal)
        
    def area_total(self):
        areat = 6 * self.a
        print('El area total es', areat)
        
    def volumen(self):
        vol = self.a **3
        print('El volumen es', vol)
        
    def __del__(self):
            print('Adios bastardo')
            
valor1 = hexaedro(102)
if valor1.a >100 or valor1.a <0:
    del valor1
    
else:
    valor1.base()
    valor1.area_lateral()
    valor1.area_total()
    valor1.volumen()

valor2 = hexaedro(101)

if valor2.a >100 or valor2.a<0:
    del valor2
else:
    valor2.base()
    valor2.area_lateral()
    valor2.area_total()
    valor2.volumen()
        
        
            
            
