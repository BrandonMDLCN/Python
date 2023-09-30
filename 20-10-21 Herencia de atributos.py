# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:41:22 2021

@author: BrandonDLC
"""
#En este solo toma el primer constructor
class principal:
    
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def metodo_prin(self):
        pass
    
class secundaria(principal):
    
    def metodo_sec(self):
        pass

obj1 = secundaria(1, 2, 3)

#%%
#Aqui toma el el constructor de la segunda clase
class principal:
    
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def metodo_prin(self):
        pass
    
class secundaria(principal):
    
    def __init__(self, w):
        self.w = w
    
    def metodo_sec(self):
        pass

obj1 = secundaria(4)

#%%
#el este se combinan los atributos a un objeto instanciado
class principal:
    
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def metodo_prin(self):
        pass
    
class secundaria(principal):
    
    def __init__(self, x, y, z, w):
        principal.__init__(self, x, y, z)
        self.w = w
    
    def metodo_sec(self):
        pass

obj1 = secundaria(1, 2, 3, 4)