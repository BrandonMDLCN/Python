# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 20:27:13 2021

@author: BrandonDLC
"""

class cajero:
    dolar = 20.25
    pesos = 0
    def __init__(self, passw, dolares):
        self.__passw = passw
        self. dolares = dolares
    
    def cambio(self):
        self.pesos = self.dolar * self.dolares
        #return print(f'Dolares a pesos: {self.pesos}')
    
    def impdatos(self):
        print(f'Valor del dolar al dia: {self.dolar}')
        print(f'Dolares a convertir: {self.dolares}')
        print(f'Dolares a pesos: {self.pesos}')
        
   #"def __del__(self):
    #    print('Contraseña Incorrecta')
    
cli1= cajero(1234, 199)
passw_ingreso = 1234

if cli1._cajero__passw == passw_ingreso:
    cli1.cambio()
    cli1.impdatos()
    if cli1.pesos > 1000:
        a=cli1.pesos/1000
        b=cli1.pesos % 1000
        print(f'Billetes de $1000: {int(a)}')
    else:
        print('Billetes de $1000: 0')
        
    if b>500:
        a=b/500
        b=b % 500
        print(f'Billetes de $500: {int(a)}')
    else:
        print('Billetes de $500: 0')
        
    if b>200:
        a=b/200
        b=b % 200
        print(f'Billetes de $200: {int(a)}')
    else:
        print('Billetes de $200: 0')
        
    if b>100:
        a=b/100
        b=b % 100
        print(f'Billetes de $100: {int(a)}')
    else:
        print('Billetes de $100: 0')
        
    if b>50:
        a=b/50
        b=b % 50
        print(f'Billetes de $50: {int(a)}')
    else:
        print('Billetes de $50: 0')
        
    if b>20:
        a=b/20
        b=b % 20
        print(f'Billetes de $20: {int(a)}')
    else:
        print('Billetes de $20: 0')
        
    if b>10:
        a=b/10
        b=b % 10
        print(f'Billetes de $10: {int(a)}')
    else:
        print('Billetes de $10: 0')
        
    if b>5:
        a=b/5
        b=b % 5
        print(f'Billetes de $5: {int(a)}')
    else:
        print('Billetes de $5: 0')
        
    if b>2:
        a=b/2
        b=b % 2
        print(f'Billetes de $2: {int(a)}')
    else:
        print('Billetes de $2: 0')
        
    if b>=1:
        a=b/1
        b=b % 1
        print(f'Billetes de $1: {int(a)}')
    else:
        print('Billetes de $1: 0')
        print(f'Le deberemos {b} centavos')

else:
    print('Contraseña Incorrecta')
    del cli1
    
    
    