# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:06:35 2021

@author: BrandonDLC
"""

#4.4 TIPOS DE EXCEPCIONES

# 2 TIPOS DE EXCEPCIONES:
    #EXCEPCIONES INTEGRADAS (POR EL SISTEMA O PROPIO LENGUAJE DE PROGRAMACION)
    #EXCEPCIONES DEFINIDAS (SE ENCUENTRA DEFINIDAS POR EL USUARIO)
    
#SENTENCIAS/SINTAXIS OBLIGATORIAS:
#   try: ESTE BLOQUE DE CODIGO REALIZARA UNA PRUEBA SOBRE ALGUN ERROR QUE
#PUDIESE EXISTIR/SURGIR
#   except: ESTE BLOQUE DE CODIGO REALIZARA UNA ACCION O VARIAS DEPENDIENDO DEL
#ERROR O EXCEPCION QUE SE HAYA SURGIDO

#SENTENCIAS/SINTAXIS OPCIONALES:
#   else: ESTE BLOQUE DE CODIGO SE EJECUTA CUANDO NO OCURRE ALGUN ERROR DENTRO
#DEL BLOQUE try

#   finally: 

class mi_clase:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def inp(self):
        #print('Hola')
        return self.x + self.y
    
try:
    obj1 = mi_case(55,27)
except:
    print('la instacia fallo por que el usuario')
else:
    pass
finally:
    pass
    

#%%

x = 5
y = 1

try:
    z = x / y

except AssertionError, AttributeError, EOFError:
    z = x / 1
    print('No se permite la dicision de cero')
    
try:
    pass
except:
    print('Personalizado')

#%%

while True:
    try:
        x = int(input('Por favor ingrese un numero entero:'))
        break
    except ValueError:
        print('El dato que ingresaste no es un numero, intenta de nuevo...')












