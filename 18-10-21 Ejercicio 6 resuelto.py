# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:02:03 2021

@author: BrandonDLC
"""

#EJERCICIO A

class cilindro:
    pi = 3.1416
    
    def __init__(self, RadioInterior, RadioExterior, Altura):
        self.ri = RadioInterior
        self.re = RadioExterior
        self.h = Altura
        
    def __mul__(self, cil):
        return cilindro(self.ri * cil.ri, self.re * cil.re, self.h)
        
cil1 = cilindro(1.13, 2.32, 3.47)
cil_ext_int = cil1 * cil1
volumen = cil1.pi/4 * cil1.h * ((cil_ext_int.re * cil_ext_int.re) - (cil_ext_int.ri * cil_ext_int.ri))

superficie = cil1.pi * cil_ext_int.re * cil1.h

print(f'Volumen: {volumen}\nSuperficie: {superficie}')

#%%

#Ejercicio B

class triangulo:

    def __init__(self, a1, a2, b1, b2, c1, c2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.c1 = c1
        self.c2 = c2
        
    def determinante1(self):
        return (self.b1 * self.c2) + (self.c1 * self.a2) + (self.a1*self.b2)
    
    def determinante2 (self):
        return (self.b1*self.a2) + (self.a1*self.c2) + (self.c1*self.b2)
    
    def area(self):
        return (triangulo.determinante1(self) - triangulo.determinante2(self))/2
    
class determinante:
    
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.d =d1
        
    def __sub__(self, det):
        return determinante(self.d1 - det.d2, self.d2)
    
tri1 = triangulo(-3, -2, 3, -2, 1, 5)
det = determinante(tri1.determinante1(), tri1.determinante2())

det1 = det - det
area = det.d1/2

print(f'Area: {area}')
    










