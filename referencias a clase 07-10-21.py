# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:44:27 2021

@author: BrandonDLC
"""

class humano:
    def __init__(self, edad, nombre, esta_empleado):
        self.edad = edad
        self.nombre = nombre
        self.esta_empleado = esta_empleado
        
    def presentar(self): #self para idicar que esta dentro de la misma clase
        presentacion = ('Hola soy {}, mi edad es {} y mi ocupacion es {}')
        print(presentacion.format(self.nombre, self.edad, self.esta_empleado))
        
    def cambiar_contrato(self, puesto):
        self.puesto =puesto
        print('{} ha sido contratado como {}'.format(self.nombre, self.puesto))
        self.esta_empleado = puesto
        
persona1 = humano(32, 'Carlos', 'si_empleado')
persona1.presentar()
persona1.cambiar_contrato('profesor')