# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:30:05 2021

@author: BrandonDLC
"""

#3.4 Constructores y destructores en clases derivadas

class vehiculo:
    
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
        
    def __str__(self):
        return f'Color: {self.color} | puertas: {self.puertas}'
    
class automovil(vehiculo):
    
    def __init__(self, color, puertas, velocidad, cilindros):
        vehiculo.__init__(self, color, puertas)
        self.velocidad = velocidad
        self.cilindros = cilindros
        
    def __str__(self):
        return f'{vehiculo.__str__(self)}\n{self.velocidad} km/h | {self.cilindros} cc'
    
carro = automovil('azul', 4, 60, 1200)
print(carro)

#%%

#Ejercicio en clase

class vehiculo:
    
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
        
    def __str__(self):
        return f'Color: {self.color} | puertas: {self.puertas}'
    
class automovil(vehiculo):
    
    def __init__(self, color, puertas, velocidad, cilindros):
        vehiculo.__init__(self, color, puertas)
        self.velocidad = velocidad
        self.cilindros = cilindros
        
    def __str__(self):
        return f'{vehiculo.__str__(self)}\n{self.velocidad} km/h | {self.cilindros} cc'
    
    
class camioneta(vehiculo, automovil):
    
    def __init__(self, color, puertas, velocidad, cilindros, caracteristica):
        vehiculo.__init__(self, color, puertas)
        automovil.__init__(self, velocidad, cilindros)
        self.carac = caracteristica
        
    def __str__(self):
        return f'{automovil.__str__(self)}\◘n{self.carac}'
    
class aereo(vehiculo):
    
    def __init__(self, color, puertas, velocidad, cilindros, tipo):
        vehiculo.__init__(self, color, puertas)
        self.velocidad = velocidad
        self.cilindros = cilindros
        self.tipo = tipo
        
    def __str__(self):
        return f'{vehiculo.__str__(self)}\n{self.velocidad} km/h | {self.cilindros} cc | {self.tipo}'
 
class jet(vehiculo, aereo):
    
    def __init__(self, color, puertas, velocidad, cilindros, tipo, supersonico):
        vehiculo.__init__(self, color, puertas)
        aereo.__init__(self, velocidad, cilindros, tipo)
        self.supersonico = supersonico
        
    def __str__(self):
        return f'{aereo.__str__(self)}\n | Supersonico: {self.supersonico}'
    
    
    
    
Rayo_McQueen = automovil('Rojo', 2, 300, 3500)
Camioneta = camioneta('Azul', 4, 250, 4000, '4x4')
JetLee = jet('blanco', 3, 400, 5005, 'deportivo', 'si')

print(Rayo_McQueen)
print(Camioneta)
print(JetLee)








