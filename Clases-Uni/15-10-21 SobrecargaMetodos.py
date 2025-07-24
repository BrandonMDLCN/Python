# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:26:51 2021

@author: BrandonDLC
"""

#2.6/2.7: SEBRECARGA DE METODOS | SOBRECARGA DE OPERADORES |

def mi_metodo(self, x, y, z):
    self.hola = x + y
    self.hola /= z
    return self.hola

    
#%%
#SOBRECARGA DE METODOS

#MISMO METODO CON INFORMACION Y RESULTADOS DIFERENTES

class sobrecarga_metodos:
    
    def dato(self, valor):
        if type(valor) == int:
            print('El valor es un entero')
        elif type(valor) == str:
            print('El valor es un string')
        else:
            print('El valor es un DATO desconocido')
            
ejemplo1 = sobrecarga_metodos()

ejemplo1.dato(14)
ejemplo1.dato('Hoy es viernes')
ejemplo1.dato(19.783)

#%%

class saludo:
    
    def dinamico(self, nombre = None):
        if nombre is not None:
            print ('Hola como estas: '+ nombre)
        else:
            print('Hola, hay alguien ahi?')
            
ejemplo1 = saludo()

ejemplo1.dinamico()
ejemplo1.dinamico('Carlos')
        
        
        
        
        
        
        
        
        