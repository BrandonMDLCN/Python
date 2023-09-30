# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:09:01 2021

@author: BrandonDLC
"""
#Clase tanque
class tanque:
    pi = 3.1416
    are = 0
    #Constructor con atributos
    def __init__(self, eje_mayor, eje_menor, altura):
        self.__em = eje_mayor
        self.emenor = eje_menor
        self.a = altura
        
    #Metodos
    #Metodo area sin la divicion para que se haga con la sobrecarga
    def area(self):
        self.are = self.pi * (self.__em) * (self.emenor)
        print(f'El area es: {self.are}')
    
    def volumen(self):
        self.volumen = self.are * self.a
        print(f'El volumen es: {self.volumen}')
    
    
    def __truediv__(self, esc): #Divición
        float_esc = float(esc)
        return tanque(self.__em / float_esc, self.emenor / float_esc, self.a)
    
#Instanciado un objeto
obj1 = tanque(15, 10, 10)


div = obj1 /2 #Usando el constructor

#Imprimiendo valores
div.area()
div.volumen()

#%%

#Clase
class eclineal:
    
    #Constructor con atributos
    def __init__(self, c1, c2, b1, c3, c4, b2):
        self.c1 = c1
        self.c2 = c2
        self.b1 = b1
        self.c3 = c3
        self.c4 = c4
        self.b2 = b2
        
    #Funcion Imprimir
    def imp(self):
        print('Ecuacion Ingresada')
        print(f'{self.c1}X  {self.c2}Y = {self.b1}')
        print(f'{self.c3}X  {self.c4}Y = {self.b2}')
        print('Solucion:')
        
    #Funciones para calcular las determinantes
    def determinante_s(self):
        self.ds = (self.c1*self.c4)-(self.c3*self.c2)
    
    def determinante_x(self):
        self.dx = (self.b1*self.c4)-(self.c2*self.b2)
    
    def determinante_y(self):
        self.dy = (self.c1*self.b2)-(self.b1*self.c3)
        
    #Sobrecarga para calcular X y Y
    def __truediv__(self, esc): #Divición
        float_esc = float(esc)
        self.p = (self.dx / float_esc, self.dy / float_esc)
        return self.p
        
        
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











        