# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:29:17 2021

@author: BrandonDLC
"""

#3.2 Clase base publica, protegidas y privadas
#HERENCIAS MULTIPLE

class Computadora:
    
    def __init__(self, cpu, gpu):
        self.cpu =cpu
        self.gpu=gpu
        
class carac_tecnicas:
    
    def muestra_specs(self):
        print('Las caracteristicas de esta PC van a ser las siguentes')
    
class mi_compu(Computadora, carac_tecnicas):
    
    def iniciar_computadora(self):
        print(f'El CPU en Hz: {self.cpu}y la GPU en VRAM es de: {self.gpu}')
        
mi_pc = mi_compu(8, 8)
mi_pc.iniciar_computadora()
mi_pc.muestra_specs()

#%%

class Estudiante:
    
    def __init__(self, edad, nombre, calif):
        self.edad = edad
        self.nombre = nombre
        self.__calif = calif
        
class Mecatronica(Estudiante):
    
    def presentar_Estudiante(self):
        print(f'El estudiante: {self.nombre} cuya edad de {self.edad}, tiene una calificacion de: {self._Estudiante__calif}')
        
primer_Estudiante = Mecatronica(21, 'Oscar', 100)
primer_Estudiante.presentar_Estudiante()

#%%

#EJERCICIO EN CLASE
#MINIMO 3 CLASES
#DONDE LAS 2 CLASES BASE CUENTE CON AL MENOS UN ATRIBUTO PROTEGIDO

class Estudiante:
    
    def __init__(self, edad, nombre, calif):
        self.edad = edad
        self.nombre = nombre
        self.__calif = calif
        
class datos_extra:
    
    def __init__(self, num_control, TSangre, num_tel):
        self.__nc = num_control
        self.ts = TSangre
        self.__nt = num_tel
        
class Mecatronica(Estudiante, datos_extra):
    
    def presentar_Estudiante(self):
        print(f'El estudiante: {self.nombre} cuya edad de {self.edad}, tiene una calificacion de: {self._Estudiante__calif}')
        print(f'con numero de control: {self._datos_extra.__nc}, tipo de sangre: {self.ts} y numero de telefono {self._datos_extra.__nt}')


primer_Estudiante = Mecatronica(21, 'Oscar', 100, '17171089', 'O+', '6670000000')
primer_Estudiante.presentar_Estudiante()



















