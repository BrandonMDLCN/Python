# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:31:08 2021

@author: BrandonDLC
"""

class articulo:
    
    def __init__(self, Nombre, año):
        self.a = Nombre
        self.b = año
        
class video(articulo):
    
    def Grabar(self):
        print('Se ha comenzado a grabar')

class audio(articulo):
    
    def __init__(self, calidad):
        articulo.__init__(self, Nombre, año)
        self.c = calidad
        
class altavoces(articulo):
    
    def reproducir(self):
        print('Se esta reproduciendo musica')
        
class radio(audio):
    
    def tocar(self):
        print(f'La radio {self.a} del año: {self.b} tiene la calidad: {self.c}')
        
class casete(audio):
    
    def a(self):
        print(f'La radio {self.a} del año: {self.b} tiene la calidad: {self.c}')
    
a = audio('')
obj = radio('buena')
obj.tocar()
    
    
    
    
    
    
    
    