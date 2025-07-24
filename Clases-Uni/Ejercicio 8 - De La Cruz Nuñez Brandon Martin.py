# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:21:44 2021

@author: BrandonDLC
"""
#%%

#PROGRAMA 1
contador = 1
print("Cual es el numero entero por el cual se va a dividir?")
num_entero = input()
e = int(num_entero)
print("el numero entero es:", num_entero)

print("ingresa numero flotante")
num_float = input()
f = float(num_float)

while True:

    try:
        resul = f / e
    except ZeroDivisionError:
        print("Se encontro una division sobre 0")
        print("Ingrese otro numero entero")
        num_entero = input()
        e = int(num_entero)
    
    except ValueError:
        print("Asegurate que no sea un caracter lo que estas intentando dividir")
        print("Ingrese otro numero entero")
        num_entero = input()
        e = int(num_entero)
    
    else:
        print("El resultado de la division fue:", resul)
        break
        
    finally:
        print('Fin del programa\n')


















#%%

#PROGRAMA 2

from abc import ABC, abstractmethod
class figura(ABC):
    @abstractmethod
    def area_rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        
        self.area = base * altura
        print(f"El area del rectangulo es: {self.area}")
    @abstractmethod
    def area_cuadrado(self, lado):
        self.lado = lado
        self.area = lado * lado
        print(f"El area del cuadrado es: {self.area}")
    @abstractmethod
    def area_triangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = (base * altura)/2
        print(f"El area del triangulo es: {self.area}")
        
class rectangulo(figura):
    def area_rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = base * altura
        print(f"El area del rectangulo es: {self.area}")
    def area_cuadrado(self, lado):
        self.lado = lado
        self.area = lado * lado
        print(f"El area del cuadrado es: {self.area}")
    def area_triangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = (base * altura)/2
        print(f"El area del triangulo es: {self.area}")

class cuadrado(figura):
    def area_rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = base * altura
        print(f"El area del rectangulo es: {self.area}")
    def area_cuadrado(self, lado):
        self.lado = lado
        self.area = lado * lado
        print(f"El area del cuadrado es: {self.area}")
    def area_triangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = (base * altura)/2
        print(f"El area del triangulo es: {self.area}")
class triangulo(figura):
    def area_rectangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = base * altura
        print(f"El area del rectangulo es: {self.area}")
    def area_cuadrado(self, lado):
        self.lado = lado
        self.area = lado * lado
        print(f"El area del cuadrado es: {self.area}")
    def area_triangulo(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = (base * altura)/2
        print(f"El area del triangulo es: {self.area}")

Rec = rectangulo()
Rec.area_rectangulo(2, 4)
Cua = cuadrado()
Cua.area_cuadrado(4)
Triang = triangulo()
Triang.area_triangulo(2, 3)







#%%

#PROGRAMA 3

class forma:
    def area(self):
        print(f"ese es el area {self.a}")

class circulo(forma):

    def areac(self, radio):
        self.a = 3.1416 *(radio * radio)
        super().area()
        
    
class cuadrado(forma):

    def areacua(self, lado):
        self.a = lado * lado
        super().area()
        
cir = circulo()
cua = cuadrado()

cir.areac(4)
cua.areacua(4)






















