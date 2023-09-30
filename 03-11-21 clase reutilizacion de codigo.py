# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:57:37 2021

@author: BrandonDLC
"""

#4.3 REUTILIZACION DE CODIGO

class ave:
    
    def info_general(self):
        print('actualmente existen una variedad de especies de ave')
        
    def volar(self):
        print('la mayoria de las aves pueden volar')
        
class gallina(ave):
    
    def volar(self):
        print('las gallinasvuelan a baja altura')
        
class paloma(ave):
    
    def volar(self):
        print('las palonas pueden volar alto')
        
#obj_ave = ave()
#obj_gallina = gallina()
#obj_paloma = paloma()

#obj_ave.info_general()
#obj_ave.volar()

#obj_gallina.info_general()
#obj_gallina.volar()

#obj_paloma.info_general()
#obj_paloma.volar()

for aves in ave(), gallina(), paloma():
    aves.info_general()
    aves.volar()
    
#%%

class mexico:
    
    def capital(self):
        print('la capital es CDMX')
        
    def idioma(self):
        print('el idioma es español')
        
    def moneda(self):
        print('la moneda es peso mexicano')
        
class portugal:
    
    def capital(self):
        print('la capital es lisboa')
        
    def idioma(self):
        print('el idioma es portugues')
        
    def moneda(self):
        print('la moneda es euro')

def funcion(obj):
    obj.capital()
    obj.idioma()
    obj.moneda()
    
#Las instancias u objetos se realizan de la forma tradicional
    
obj_MX = mexico()
obj_PT = portugal()

#Los metodos se mandan a llamar a travez de una funcion

funcion(obj_MX)
funcion(obj_PT)

#%%
#EJERCICIO EN CLASE
#MODIFIQUE EL PRESENTE CODIGO, DE MODO QUE SE UTILIVEN CLASES Y METODOS
#ABSTRACTOS, ADEMAS, REALICE LAS MODIFICACIONES NECESARIAS PARA QUE SE
#UTILICEN MENOS LINEAS DE CODIGO

class persona:
    
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def imp_mensaje(self):
        if self.tipo == 'menor':
            print(f'{self.nombre} es joven')
        elif self.tipo == 'mayor':
            print(f'{self.nombre} es adulto')
            
class hijo(persona):
    
    def imp_mensaje(self):
        if self.tipo == 'señor':
            print(f'{self.nombre} es niño')
        elif self.tipo == 'mayor':
            print(f'{self.nombre} es adolecente')
            
persona1 = hijo('Jose', 'menor')
persona2 = persona('Jesus', 'mayor')

print(persona1.nombre, persona1.tipo, persona2.nombre, persona2.tipo)
        
#%%





























