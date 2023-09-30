# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:16:39 2021

@author: BrandonDLC
"""

#Capture info de un cel
#

class telefono:
    
    def __init__(self, numero):
        self.numero =numero
        
    def llamar(self):
        print('Llamando a algun telefono en algun lado')
        
    def colgar (self):
        print('Colgando llamada')
        
    def __str__(self):
        return f'Mi numero es: {self.numero}'
    
class camara:
    
    def __init__(self, mpx):
        self.mpx = mpx
    
    def foto(self):
        print('Tomando fotografia')
        
    def __str__(self):
        return f'La resolucion de la camara es: {self.mpx}'
    
class reproductor:
    
    def __init__(self, mp3):
        self.mp3 = mp3
        
    def musica(self):
        print('Reproduciendo cancion....')
        
    def __str__(self):
        return f'La resolucion de la camara es: {self.mp3}'
        
class celular(telefono, camara, reproductor):
    
    def __init__(self, numero, mpx, mp3):
        telefono.__init__(self, numero)
        camara.__init__(self, mpx)
        reproductor.__init__(self, mp3)
    
    def __str__(self):
        return f'Numero TEL: {self.numero}, camara de: {self.mpx}, la cancion es: {self.mp3}'
    
mi_cel = celular('6671905612', '30', 'cualquier cancion')

print(mi_cel)

#%%

class tm:
    def __init__(self, trjetam):
        self.tarjetaMadre = trjetam
        
    def __str__(self):
        return f'La marca de la tarjeta madre es: {self.tajetaMadre}'
    
class cpu:
    def __init__(self, CPU):
        self.CPU = CPU
        
    def __str__(self):
        return f'El cpu es es: {self.CPU}'
    
class ram:
    def __init__(self, RAM):
        self.RAM = RAM
    
    def __str__(self):
        return f'La capacidad de memoria RAM es: {self.RAM}'

class gpu:
    def __init__(self, GPU):
        self.GPU = GPU
        
    def __str__(self):
        return f'La capacidad de GPU es: {self.GPU}'
    
class Memoria:
    def __init__(self, memoria):
        self.memoria = memoria
        
    def __str__(self):
        return f'El tipo de memoria es: {self.memoria}'
    
class psu:
    def __init__(self, PSU):
        self.PSU = PSU
        
    def __str__(self):
        return f'El PSU es: {self.PSU}'
    
class computadora(tm, cpu, ram, gpu, Memoria, psu):
    def __init__(self, tarjetaMadre, CPU, RAM, GPU, memoria, PSU):
        tm.__init__(self, tarjetaMadre)
        cpu.__init__(self, CPU)
        ram.__init__(self, RAM)
        gpu.__init__(self,GPU)
        Memoria.__init__(self, memoria)
        psu.__init__(self, PSU)
        
    def __str__(self):
        return f'La tarjeta madre es: {self.tarjetaMadre}, el CPU es: {self.CPU}, Memoria RAM de: {self.RAM}, GPU de: {self.GPU}, memoria de: {self.memoria}, PSU de: {self.PSU}'
    
cpu1 = computadora('TM5000', '20', '16 GB', '700', '500 GB SSD', '80')
print(cpu1)

    
    
    
    
    
    
    
    