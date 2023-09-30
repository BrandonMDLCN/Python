# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:34:04 2021

@author: BrandonDLC
"""

#polimorfismo (se puede decir que en vez de pasar atributos reciclamos los metodos)
#No podemos trabajar polimorfismo si no hacemos herencias

class mi_clase:
    
    def mi_metodo(self):
        pass
    
class mi_clase_2:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def mi_metodo(self):
        pass
    
#%%

class persona:
    
    def hablar(self):
        print('Hola buenos dias')
        
class estudiante(persona):
    
    def hablar(self):
        super().hablar()  #con super podemos usar cualquier metodo de la principal en una clase secundaria
        print('Soy estudiante de la carrera mecatronica')
        
class empleado(persona):
    
    def hablar(self, saludo):
        print(saludo)
        
estudiante1 = estudiante()

empleado1 = empleado()

#A partir de este punto se trabaja con polimorfismo

estudiante1.hablar()
empleado1.hablar('Mi numero de empleado es 1234')

#%%

#Ejercicio en clase:
#Hacer en programa donde se definan 2 clases en el contexto de paises
#Ejemplo: mexico, panama, donde casa clase debera tener 3 metodos:
#Ejemplo: capital, idioma, tipo; cada metodo debera imprimir su propio mensaje
#mensaje en consola dependiendo del contexto.

class mexico:
    
    def idioma(self):
        print('Español')
    
    def moneda(self):
        print('Pesos')
        
    def salario(self):
        print('70')
        
    def imprimir(self):
        print(f'El idioma es: {super().idioma()}')
        
class usa:
    
    def idioma(self):
        print('Ingles')
    
    def moneda(self):
        print('Dolares')
        
    def salario(self):
        print('500')
        
Mexico = mexico()

USA = usa()

Mexico.imprimir()
