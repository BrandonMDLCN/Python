# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 01:23:17 2021

@author: BrandonDLC
"""
#Iniciamos la clase
class cilindro:
    pi = 3.1416
    #Definimos los atributos
    def __init__(self, altura, Diametro, diametro):
        self.a = altura
        self.D = Diametro
        self.d = diametro
        
    #Definimos 2 metodos
        #Metodo para sacar Volumen
    def volumen(self):
        volumen = (self.pi * ((self.D**2) - (self.d**2)))/4
        return volumen
    
        #Metodo para sacar Superficie
    def superficie(self):
        re = self.D/2
        sup = self.pi * re**2
        return sup
    
    #Se multiplica el metodo por los atributos
    def __mul__(self, x):
        return cilindro(self.a * x, self.D, self.d)
    
#Instanciamos la clase
cilindro1 = cilindro(8, 4, 2)

#Mandamos a llamar a los metodos y se aplica la sobrecarga
vol = cilindro1 * cilindro1.volumen()
superf = cilindro1 * cilindro1.superficie()

#Imprimimos el volumen y la superficie
print('El volumen del cilindro es: ', vol.a)
print('La superficie del cilindro es: ', superf.a)

#%%

class triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def __mul__(self, x):
        return triangulo(self.b * x.c, self.c * x.a, self.a * x.b)
    def suma(self):
        suma = self.a + self.b + self.c
        return suma
        
t1 = triangulo(5, 7, 8)
t2 = triangulo(3, 2, 1)

d1 = t1 * t2
d2 = t2 * t1

A = (d1.suma() - d2.suma())/2

print('El area del tringulo es:', A)
    
    
    
    
    
    
    
    
    
    
        