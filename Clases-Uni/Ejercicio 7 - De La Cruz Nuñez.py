# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:05:01 2021

@author: BrandonDLC
"""

class robot:
    
    def __init__(self, sistema, memoria, peso):
        self.sistema = sistema
        self.memoria = memoria
        self.peso = peso
        
class computadora:
    
    def __init__(self, ram, sistemaa, costo):
        self.ram = ram
        self.sistemaa = sistemaa
        self.costo = costo
        
class militares(robot):
    
    def __init__(self, sistema, memoria, peso, bunques, armamento, secretos):
        robot.__init__(self, sistema, memoria, peso)
        self.bunques = bunques
        self.armamento = armamento
        self.secretos = secretos
        
class industrial(robot):
    
    def __init__(self, sistema, memoria, peso, fabrica, funcion, giro):
        robot.__init__(self, sistema, memoria, peso)
        self.fabrica = fabrica
        self.funcion = funcion
        self.giro = giro
        
    def __str__(self):
        return f'Sistema {self.sistema}, Memoria: {self.memoria}, peso: {self.peso}, fabrica: {self.fabrica}, funcion: {self.funcion}, Giro: {self.giro}'
    
        
class medicos(robot):
    
    def __init__(self, sistema, memoria, peso, area, lugar, num_seguro):
        robot.__init__(self, sistema, memoria, peso)
        self.area = area
        self.lugar = lugar
        self.num_suguro = num_seguro
        
    def __str__(self):
        return f'Sistema {self.sistema}, Memoria: {self.memoria}, peso: {self.peso}, area: {self.area}, lugar: {self.lugar}, Numero del seguro: {self.num_suguro}'
    
        
class arduino(robot, computadora):
    
    def __init__(self, sistema, memoria, peso, ram, sistemaa, costo, marca, puertas, contraseña):
        robot.__init__(self, sistema, memoria, peso)
        computadora.__init__(self, ram, sistemaa, costo)
        self.marca = marca
        self.puertas = puertas
        self.__contraseña = contraseña
        
    def __str__(self):
        return f'Sistema {self.sistema}, Memoria: {self.memoria}, peso: {self.peso}, Ram: {self.ram} Sistema del arduino: {self.sistemaa}, Costo: {self.costo}, Marca: {self.marca}, Numero de puertos: {self.puertas}, Contraseña: {self.__contraseña}'
    
        
class aereos(militares):
    
    def __init__(self, sistema, memoria, peso, bunques, armamento, secretos, turbinas, puertas, velocidad):
        militares.__init__(self, sistema, memoria, peso, bunques, armamento, secretos)
        self.turbinas = turbinas
        self.puertas = puertas
        self.velocidad = velocidad
        
    def __str__(self):
        return f'Sistema {self.sistema}, Memoria: {self.memoria}, peso: {self.peso}, Bunques: {self.bunques}, Armamento: {self.armamento}, Secretos: {self.secretos}, turbinas: {self.turbinas}, puertas: {self.puertas}, velocidad: {self.velocidad}'
    
    def __del__(self):
        pass
    
aerea1 = aereos('ADA', 1000, 10000, 'no', 'si', 'burritos son comida', 4, 3, 400)
industrial1 = industrial('C++', 500, 'no', 'Kappa', 'Papel', 'Comercial')
medicos1 = medicos('python', 250, 400, 'quirurjica', 'Culiacan', 84)
arduino1 = arduino('Arduino', 250, 100, 16, 'si', 800, 'Uno', 20, 1234)

clave = 12345

if arduino1._arduino__contraseña == clave:
    print('Aereo:\n', aerea1)
    print('Industrial:\n ', industrial1)
    print('Médico:\n', medicos1)
    print('Arduino:\n', arduino1)
  
else:
    del aerea1, industrial1, medicos1, arduino1, aereos
    print('Contraseña incorrecta')
    
    
    