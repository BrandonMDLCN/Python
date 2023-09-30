# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:22:11 2021

@author: BrandonDLC
"""


class eclineal:
    
    def __init__(self, c1, c2, b1, c3, c4, b2):
        self.c1 = c1
        self.c2 = c2
        self.b1 = b1
        self.c3 = c3
        self.c4 = c4
        self.b2 = b2
        
    def imp(self):
        print('Ecuacion Ingresada')
        print(f'{self.c1}X  {self.c2}Y = {self.b1}')
        print(f'{self.c3}X  {self.c4}Y = {self.b2}')
        print('Solucion:')
        
    def determinante_s(self):
        self.ds = (self.c1*self.c4)-(self.c3*self.c2)
    
    def determinante_x(self):
        self.dx = (self.b1*self.c4)-(self.c2*self.b2)
    
    def determinante_y(self):
        self.dy = (self.c1*self.b2)-(self.b1*self.c3)
        
    def __truediv__(self, esc): #Divición
        float_esc = float(esc)
        self.p = (self.dx / float_esc, self.dy / float_esc)
        return self.p
    
    def __del__(self):
        print('Adios')
        
        
#Instanciar Objeto
obj = eclineal(8, -5, -5, 3, -4, 13)

#Realizar Operaciones
obj.determinante_s()
obj.determinante_x()
obj.determinante_y()

#Calcular X y Y
divx = obj.dx / obj.ds
divy =obj.dy / obj.ds


#Imprimir Objetos
obj.imp()
print(f'X = {divx}')
print(f'Y = {divy}')
del divx, divy, obj