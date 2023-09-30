# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:53:19 2021

@author: BrandonDLC
"""

class num_complejo:
    
    def __init__(self, parte_real, parte_img):
        self.real = parte_real
        self.ing = parte_img
        
num_uno = num_complejo(7.0, -2.7)

#%%

class saludo:
    
    def __init__(self, mi_saludo):
        self.saludar = mi_saludo
        
    def muestra_saludo(self):
        print(self.saludar)
        
ejemplo1 = saludo('Hola como estas?')

ejemplo1.muestra_saludo()
    

#%%

class circulo:
    #atributos que se encuentran fuera del cosntructor INIT
    #sin atributos de clase
    pi = 3.1416
    
    def __init__(self, radio):
        self.r = radio
        
    def calcular_area(self):
        #self.r ** 2 sintaxis para elevar al cuadrado
        return circulo.pi * self.r ** 2
    
primer_circulo = circulo(7)

segundo_circulo = circulo(4)

primer_circulo_area = primer_circulo.calcular_area()

segundo_circulo_area = segundo_circulo.calcular_area()

print(primer_circulo.calcular_area())

print(segundo_circulo.calcular_area())

print(primer_circulo.pi)

print(segundo_circulo.pi)

#%%

class sumar:
    num_1 = 0
    num_2 = 0
    resultado = 0
    def __init__(self, primero, segundo):
        self.num_1 = primero
        self.num_2 = segundo
        
    def mostrar(self):
        print('Primer Numero = ' + str(self.num_1))
        print('Segundo Nmero = ' + str(self.num_2))
        print('El resultado es = ' + str(self.resultado))
        
    def calculo(self):
        self.resultado = self.num_1 + self.num_2
        
ej1 = sumar(50, 12)

ej1.calculo()

ej1.mostrar()
        
        
        
        
        
        
        
        
        
        
        
        









