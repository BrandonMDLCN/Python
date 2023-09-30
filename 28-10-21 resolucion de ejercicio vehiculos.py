# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:06:19 2021

@author: BrandonDLC
"""

class vehiculo:
    
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
        
    def __str__(self):
        return f'Color: {self.color} | Puertas: {self.puertas}'
    
class automovil(vehiculo):
    
    def __init__(self, color, puertas, ruedas):
        vehiculo.__init__(self, color, puertas)
        self.ruedas = ruedas
        
    def __str__(self):
        return f'{vehiculo.__str__(self)}  |  ruedas: {self.ruedas}'
    
class aereo(vehiculo):
    
    def __init__(self, color, puertas, propulsion):
        vehiculo.__init__(self, color, puertas)
        self.propulsion = propulsion
        
    def __str__(self):
        return f'{vehiculo.__str__(self)}  |  ruedas: {self.propulsion}'
    
class camioneta(automovil):
    
    def __init__(self, color, puertas, ruedas, velocidad):
        vehiculo.__init__(self,color, puertas)
        automovil.__init__(self, color, puertas, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return f'{automovil.__str__(self)}   |   velocidad: {self.velocidad} km/h'
    
    def __del__(self):
        print('Camioneta Destruido')
    
class jet(aereo):
    
    def __init__(self, color, puertas, propulsion, velocidad):
        vehiculo.__init__(self, color, puertas)
        aereo.__init__(self, color, puertas, propulsion)
        self.velocidad = velocidad
        
    def __str__(self):
        return f'{aereo.__str__(self)}    |    Velocidad: {self.velocidad} km/h'
    
    def __del__(self):
        print('Jet Destruido')
        
        


viaje_tierra = camioneta('Azul', 4, 4, 96)
viaje_aire = jet('blanco', 2, 'turbina', 40)

viaje_distancia = 280

tiempo_tierra = viaje_distancia / viaje_tierra.velocidad
tiempo_aire = viaje_distancia / viaje_aire.velocidad

if tiempo_tierra < tiempo_aire:
    
    print('Viaje por tierra es mejor')
    del viaje_aire
    
else:
    print('Viaje por aire es mejor')
    del viaje_tierra
    
    