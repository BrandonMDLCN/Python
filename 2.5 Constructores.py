# -*- coding: utf-8 -*-hola
"""
Created on Wed Oct 13 16:40:52 2021

@author: BrandonDLC
"""
#METODO DE PROGRAMAR TIPO "A"

class persona:
    edad = 0
    estatura = 0
    peso = 0
    nombre = ''
    
    def imprime_datos():
        print('El nombre de la persona es: ')
        
persona1 = persona()

persona1.edad = 21
persona1.peso = 74
persona1.estatura = 1.76
persona1.nombre = 'Jose'



#----------------------------------------------------------

#METODO DE PROGRAMAR TIPO "B"

class persona:
    def __init__(self, edad, estatura, peso, nombre):
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
        self.nombre = nombre
        
        def imprime_datos(self):
            print('El nombre de la persona es: ', self.nombre)
            
persona1 = persona(21, 1.76, 74, 'Jose')