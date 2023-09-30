# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:15:50 2021

@author: BrandonDLC
"""

class interacion:
    Incrementador =0
    
    def contador(self):
        self.Incrementador +=1
        print("El calor o numero es en este momento:", self.Incrementador)
        
ejemplo1=interacion()

for i in range(50):
    ejemplo1.contador()