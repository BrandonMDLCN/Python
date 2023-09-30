# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:15:43 2021

@author: BrandonDLC
"""

#CONSTRUCTORES Y DESTRUCTORES

#%%
#ESTE ES LA SINTAXIS BASICA DE UN DESTRUCTOR EN PYTHON
def __del__(self):
    print('estoy a punto de ser destruido')

#%%

class contador:
    incre = 0
    def __init__(self):
        print('Hola como estas?')
        
    def incrementa(self):
        self.incre = self.incre + 1
        print ('El valor actual es: ', self.incre)
        
    def __del__(self):
        print('Que tenga buen dia, adios!!', self.incre)
        
ejemplo1 = contador()

ejemplo1.incrementa()

#Al ejecutar esta linea, se destruye ejemplo1 para convertirse en una cosntante
#Cono se sobre escribe, se ejecuta el destructor
ejemplo1 = 89
print(ejemplo1)

#%%

class Estudiante:
    def __init__(self):
        print('Estudiante registrado!!')
        
    def __del__(self):
        print('Estudiante limpio o sin registro')
            
def iniciar_registro():
    print('Se inicializara un registro...')
    ejemplo1 = Estudiante()
    print('Hasta este punto se termina el registro')
    return ejemplo1

print('El registro esta por iniciar')
ejemplo1 = iniciar_registro()
print('El registro del estudiante se termino')

del ejemplo1
            
#%%


            
            
            
            
            
            
            
            
            
            



