# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:05:32 2021

@author: BrandonDLC
"""

class hexaetro:
    
    def __init__(self, arista):
        self.a = arista
        self.b = self.a * self.a
        self.al = 4 * (self.a **2)
        self.at = 6 * (self.a **2)
        self.v = self.a **3
        
    def __del__(self):
        print('Objeto Destruido')
        
hex1 = hexaetro(100)

if hex1.a >100 or hex1.a <=0:
    del hex1
else:
    print(f'A: {hex1.a}, H: {hex1.b}, AL: {hex1.al}, Al: {hex1.at}, V: {hex1.v}')