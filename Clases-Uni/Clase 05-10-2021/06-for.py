import time
#iterar una lista de elementos
#Buscar elementos 
"""
for numero in range(5):
    print(numero, numero *'hola mundo')
"""
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print ("Encontrado", buscar)
        break
    else:
        print("no encontro numero buscado")
    time.sleep(1) #Hace que dure un segundo cada ejecución, para esto ocupa la libreria "time"

for char in "Ultinate python":
    print(char)

for digit in "0165031806510": 
    if digit == "0": # Línea de código.
        digit = "x" #Remplaza el 0 por x
    print(digit, end="")    #hasta que termina el ciclo manda el print completo