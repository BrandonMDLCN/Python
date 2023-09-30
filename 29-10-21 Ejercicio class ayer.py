# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:06:53 2021

@author: BrandonDLC
"""

class pais:
    
    def capital(self):
        print('Un pais siempre tiene una capital')
    
    def idioma(self):
        print('Un un pais se habla un idioma en especifico')
        
    def habitantes(self):
        print('Un pais tiene un cirto numero de habitantes')
        
class canada(pais):
    
    def capital(self):
        print('La capital de Canada es Monterey')
        
    def idioma(self):
        print('El idioma en canada es frances y ingles')
        
    def habitantes(self):
        print('El numero de habitantes de Canada es: 5M')
        
class españa(pais):
    
    def capital(self):
        print('La capital de España es Madrid')
        
    def idioma(self):
        print('El idioma en canada es Español')
        
    def habitantes(self):
        print('El numero de habitantes de España es: 4.5M')
        
#pais1= canada()
#pais2 = españa()

#pais1.capital()
#pais1.idioma()
#pais1.habitantes()

#pais2.capital()
#pais2.idioma()
#pais2.habitantes()

#Recorrer los metodos de forma sencilla
for Paises in canada(), españa():
    Paises.capital()
    Paises.idioma()
    Paises.habitantes()

#%%

#CLASES ABSTRACTAS: DEFINICION, METODOS, IMPLEMENTACION Y MODELADO

#OBJETIVOS: REUTILIZACION DE CODIGO O RECICLAJE DE CODIGO

#NO SE PUEDE INSTANCIAR DE LA CLASE ABSTRACTA

from abc import ABC, abstractmethod #REQUISITO OBLIDATORIO EN PYTHON

class persona(ABC):
    
    @abstractmethod
    def saltar(self):
        pass
    
    @abstractmethod
    def hablar(self):
        print('La persona envia un saludo afectuaso')
        
class estudiante(persona):
    
    def saltar(self):
        print('El estudiante esta saltando en su clase')
        
    def hablar(self):
        print('El estudiante saluda a sus compañeros')
        
estudiante1 = estudiante()

estudiante1.saltar()
estudiante1.hablar()


















        
        
        
        
        
        

        
        