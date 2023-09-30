# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:57:42 2021

@author: BrandonDLC
"""

class articulo:
    
    def __init__(self, frecuencia):
        self.f = frecuencia
        
class video(articulo):
    
    def imp(self):
        print(f'frec: {self.f}')
        
class audio(articulo):
    
    def __init__ (self, frecuencia, volumen):
        articulo.__init__(self, frecuencia)
        self.v = volumen
        
    def imp (self):
        print(f'frec: {self.f}, vol: {self.v}')
        
class altavoces(articulo):
    
    def imp(self):
        print(f'frec: {self.f}')
        
class radio (audio):
    
    def __init__(self, frecuencia, volumen, estacion):
        articulo.__init__(self, frecuencia)
        audio.__init__(self, frecuencia, volumen)
        self.e = estacion
        
    def imp(self):
        print(f'frec: {self.f}, vol: {self.v}, est: {self.e}')
        
class casete (audio):
    
    def __init__(self, frecuencia, volumen, cinta):
        articulo.__init__(self, frecuencia)
        audio.__init__(self, frecuencia, volumen)
        self.c = cinta
        
    def imp(self):
        print(f'frec: {self.f}, vol: {self.v}, cinta: {self.c}')
        
        
class cd (audio):
    
    def __init__(self, frecuencia, volumen, album):
        articulo.__init__(self, frecuencia)
        audio.__init__(self, frecuencia, volumen)
        self.a = album
        
    def imp(self):
        print(f'frec: {self.f}, vol: {self.v}, album: {self.a}')
        
class amplificador (audio):
    
    def __init__(self, frecuencia, volumen, ganancia):
        articulo.__init__(self, frecuencia)
        audio.__init__(self, frecuencia, volumen)
        self.g = ganancia
        
    def imp(self):
        print(f'frec: {self.f}, vol: {self.v}, ganancia: {self.g}')
        
ob_video = video(1000)
obj_audio = audio(1000, 50)
obj_altavoces = altavoces(2000)

obj_radio = radio(3000, 75, 109.1)
obj_casete = casete(2000, 60, 'ok')
obj_cd = cd(1000, 50, 'green days')
obj_ampli = amplificador(8000, 180, 90)

ob_video.imp()
obj_audio.imp()
obj_altavoces.imp()

obj_radio.imp()
obj_casete.imp()
obj_cd.imp()
obj_ampli.imp()





        
        
        
        
        