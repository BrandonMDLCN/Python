# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:31:26 2021

@author: BrandonDLC
"""



#DE LA CRUZ NUÑEZ BRANDON MARTIN

#%%
#PRIMER EJERCICIO

from abc import ABC, abstractmethod

class seg(ABC):
    
    @abstractmethod 
    def s(self):
        pass
    

class t:
    def __init__(self, segundo):
        self.segundo = segundo
        
    def intro(self):
        print("Hora buenos dias")
    
    
class conver(seg, t):
    
    def calculo(self):
        if self.segundo >= 3600:
            self.hora = int(self.segundo / 3600)
            mod = self.segundo % 3600
        else:
            self.hora = 0
            mod = self.segundo
        if mod >= 60:
            self.minutos = int(mod / 60)
            mod = mod % 60
        else:
            self.minutos = 0
            
        self.segundos = mod
               
    def s(self):
        super().intro()
        print(f"El tiempo es de: {self.hora} hrs. {self.minutos} min. {self.segundos} seg.")


print("Ingrese la cantidad en Segundos")
a = int(input())
tiempo = conver(a)

try:
    tiempo.calculo()
    tiempo.s()

except KeyboardInterrupt:
    print("Usted ha salido")

except AttributeError:
    print("Hay un error con los atributos")
    
except ValueError:
    print("Asegurate que estas ingresando valores numericos")
    
    
    
    
#%%
#EJERCICIO 2

from abc import ABC, abstractmethod

class t(ABC):
    @abstractmethod 
    def b(self):
        pass

class info:
    def __init__(self, hora, minuto, segundo, incre):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.incre = incre
        
    def inf(self):
        print(f"El tiempo ingresado fue: {self.hora} Hrs. {self.minuto} Min. {self.segundo} Seg. Se incrementaran {self.incre} Min.")

class tiempo(t, info):
        
    def caculo(self):
        if self.incre >= 60:
            i = self.incre / 60 
            b = self.incre % 60
            self.hora = self.hora + int(i)
            self.minuto = self.minuto + b
        else:
            self.minuto = self.minuto + self.incre
        
        if self.minuto >= 60:
            self.hora = self.hora + 1
            self.minuto = 0
    
    def inf(self):
        super().inf()
        
    def b (self):
        print(f"El tiempo incrementado es: {self.hora} Hrs. {self.minuto} Min. {self.segundo} Seg")

    
print("Ingrese horas:")
h = int(input())
print("Ingrese minutos:")
m = int(input())
print("Ingrese horas:")
s = int(input())
print("Ingrese minutos a incrementar:")
i = int(input())

Tiempo = tiempo(h, m, s, i)
Tiempo.inf()

try:
    Tiempo.caculo()
    Tiempo.b()
except KeyboardInterrupt:
    print("Usted ha salido")

except AttributeError:
    print("Hay un error con los atributos")

except ValueError:
    print("Asegurate que estas ingresando valores numericos")

