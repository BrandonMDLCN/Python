# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:07:02 2021

@author: BrandonDLC
"""

while True:
    
    try:
        decimal = float(input("Bienvenido, ingresa un valor: "))
        entero = 4
        resultado = decimal / entero
        print(f"{decimal/entero} = {resultado}")
    except:
        print("Ha ocurrido un error, escribe correctamente el numero")
    except ZeroDivisionError, FloatingPointError, ValueError, TypeError, StopIteration:
        print("ERROR: No se puede dividir sobre cero, vuelve a intentar")
    else:
        print("la operación se ha realizado correctamente")
        break
    finally:
        print("Gracias por utilizar el programa, que tenga buen dia")
        
#%%

from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod 
    def Area(self):
        pass
class Calc_Area(Figura):
    
    def __init__(self, x, y):
        self.b = x
        self.h = y
        
    def Area(self):
        return self.b * self.h
    
Rectangulo = Calc_Area(10, 20)
Cuadrado = Calc_Area(5, 5)
Triangulo = Calc_Area(7, 9)

print(f"Area.Rectangulo: {Rectangulo.Area()}\n Area.Cuadrado: {Cuadrado.Area()}\n Area.Triangulo: {Triangulo.Area()/2}")

try:
    Rectangulo = Calc_Area(10, 20)
    Cuadrado = Calc_Area(5, 5)
    Triangulo = Calc_Area(7, 9)
except NotImplementedError:
    print("Esta excepcion surge cuando se esta trabajando con metodos abstractos")
    
#%%

from math import pi

class Forma:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def area(self):
        pass
    
    def info(self):
        return "la figura es una forma de 2 dimensiones"
    
    def __str__(self):
        return f"{self.nombre}"
    
class Cuadrado(Forma):
    
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.l = lado
    
    def area(self):
        return self.l ** 2
    
    def info(self):
        return "Los cuadrados suelen tener un anguo igual a 90 grados"
    
class Circulo(Forma):
    
    def __init__(self, radio):
        super().__init__("Circulo")
        self.r = radio
        
    def area(self):
        return pi * self.r ** 2
    
a = Cuadrado(4)
c = Circulo(7)

print(a)
print(a.info())
print(a.area())
        
print(c)
print(c.info())
print(c.area())  
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    