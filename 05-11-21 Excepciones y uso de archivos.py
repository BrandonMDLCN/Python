# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:53:02 2021

@author: BrandonDLC
"""

#TRABAJAR CON EL MANEJO DE ARCHIVOS (TXT, JPG, TIFFM CSV, ETC.)

try:
    #Abrimos un archivo y hacemos un objeto con la info del archivo
    #f = open('C:Users\\CamF\\Desktop\\numeros.txt')
    #Para la direccion se debe usar doble barra invertida
    f = open('C:\\Users\\BrandonDLC\\Downloads\\numeros.txt')
    #Accedemos linea por linea en el archivo y lo aguarda
    s = f.readline()
    #Convierte a entero los numeros que encuentre
    i = int(s.strip())
except IOError:
    print('Error de entrada/salida: Se recomiend que se revise el archivo ya que no se encuentra')
except ValueError:
    print('No se puede convertir a numeros caracteres especiales o letras, favor de rivisar el archivo')


#%%

#VERIFICAR QUE TIPOS DE EXCEPCIONES SE PRODUCEN AL EJECUTAR LAS SIGUIENTES
#SENTENCIAS, POSTERIORMENTE, UTILIZAR LAS INSTRUCCIONES TRY Y EXCEPTS PARA
#MANIPULAR LAS EXCEPCIONES INTEGRADAS.

# 10 * (1/0)

try:
    p = 10 * (1/0)
    
except ZeroDivisionError:
    print('No se puede dividir entre 0 pendejo')

# 4 + var1 + 3

try:
    4 + var1 + 3
    
except NameError:
    print('Posiblemente no se ha inicializano una variable, favor de revisar')
    
# '2' + 2

try:
    '2' + 2
    
except TypeError:
    print('No se pueden sumar textos con numeros imbezilo')

#%%

# raise: forzar el programa a que se ejecute una expeccion en particular

try:
    raise NameError("Buenos dias a todos")
except:
    print("una excepcion de NameError se ha encontrado")
    raise

#%%

#Ejemplo de una excepcion definida por el usuario
class mi_error_personalizado(Exception):
    
    def __init__(self, x):
        self.x = x
        
    def __str__(self):
        return f"{self.x}"

try:
    raise mi_error_personalizado(9*9)
    
except mi_error_personalizado as obj:
    print (f"Se ha ejecutado mi error personalizado debido al numero que ingresaste: {obj.x}")
    
#%%

def dividir(x, y):
    
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("Se encontro una dicision sobre 0")
    else:
        print("El resultado de la division fue:", resultado)
    finally:
        print("Se ha iniciado el calculo de una operacion: division")
        
#dividir(2, 1)

#dividir(2, 0)

dividir("2", "1")

#%%

#MODIFICAR CODIGO, DE MODO QUE SE IMPLEMENTEN AL MENOS 3 POSIBLES
#EXCEPCIONES QUE PUDIERA SURGIR

class mexico:
    
    def capital(self):
        print("La capital de Mexico es: CDMX")
        
    def idioma(self):
        print("Español")
        
    def moneda(self):
        print("Peso (MXN)")
        
class francia:
    
    def capital(self):
        print("La capital de francia es: Paris")
        
    def idioma(self):
        print("Frances")
        
    def moneda(self):
        print("Euro")

obj_MX = mexico()
obj_FR = francia()

try:
    print("Hola, ingresa contraseña. (para salir use ctrl+c")
    input()
except KeyboardInterrupt:
    print("Usted ha salido")
    
try:
    obj_MX.capital(3)
except TypeError:
    print("Favor de revisar la forma de usar objetos")
    
try:
    obj.FR
except NameError:
    print("Este objeto no est definido o no existe")



