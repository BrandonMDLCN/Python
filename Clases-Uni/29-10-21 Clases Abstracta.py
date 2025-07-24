# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:44:12 2021

@author: BrandonDLC
"""

#CLASES ABSTRACTAS: DEFINICION, METODOS, IMPLEMENTACION Y MODELADO

#OBJETIVOS: REUTILIZACION DE CODIGO O RECICLAJE DE CODIGO

#NO SE PUEDE INSTANCIAR DE LA CLASE ABSTRACTA

#REGLAS BASICAS:
#1.- No se puede instanciar objetos a partir de las clases abstractas
#2.- Se deben de utilizar TODOSlos metodos abstactos en las clases secundarias

from abc import ABC, abstractmethod #REQUISITO OBLIDATORIO EN PYTHON

class persona(ABC):
    #Se tienen que utilizar siempre los metodos en las clases instanciadas
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

ob1 = persona()

#%%

from abc import ABC, abstractmethod

class poligono(ABC):
    
    def lados(self):
        pass
    
class triangulo(poligono):
    
    def lados(self):
        print('El trianfulo tiene 3 lados')
        
class pentagono(poligono):
    
    def lados(self):
        print('El pentagono tiene 5 lados')
        
class hexagono(poligono):
    
    def lados(self):
        print('El hexagono tiene 6 lados')
        
class cuadrado(poligono):
    
    def lados(self):
        print('El cuadrado tiene 4 lados')
        
t = triangulo()
t.lados()

p = pentagono()
p.lados()

h = hexagono()
h.lados()

c = cuadrado()
c.lados()

#%%

#EJERCICIO EN CLASE
#PROGRAMA QUE UTILICE UNA CLASE ABSTRACTA Y SE IMPLENETEN
#4 CLASES SECUNDARIAS A PARTIR DE LA CLASE BASE (ABC)

from abc import ABC, abstractmethod

class automoviles(ABC):
    
    def puertas(self):
        pass
    
class carro(automoviles):
    
    def puertas(self):
        print('El carro tiene 4 puertas')
        
class avion(automoviles):
    
    def puertas(self):
        print('El avion tiene 3 puertas')
        
class barco(automoviles):
    
    def puertas(self):
        print('El barco tiene 2 puertas')
        
class moto(automoviles):
    
    def puertas(self):
        print('La moto tiene 0 puertas')
        
c = carro()
c.puertas()

a = avion()
a.puertas()

b = barco()
b.puertas()

m = moto()
m.puertas()























