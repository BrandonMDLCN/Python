# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:19:20 2021

@author: BrandonDLC
"""

#UNIDAD 3: HERENCIA SIMPLE

class Estudiante:
    
    def __init__(self, nombre, edad, carrera):
        self.n = nombre
        self.e = edad
        self.c = carrera
        
class Universidad(Estudiante):
    
    def ImpRegistro(self):
        print(f'El registro del E. {self.n}, de edad: {self.e} cuya carrera es: {self.c} se realizo con exito')
        
obj_est = Universidad('Jose', 22, 'Mecatronica')
obj_est.ImpRegistro()