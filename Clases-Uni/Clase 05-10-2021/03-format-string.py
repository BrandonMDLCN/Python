nombre = "Nicolas"
apellido = "Schurmann"
nombre_completo = f"{nombre}  {apellido}"
print(nombre_completo)
#04 Metodos string
animal = "    chancito feliz    "
print(animal.split()) #Crea lista con cada palabra
print(animal.upper()) #Todo a mayuscula
print(animal.lower()) #Todo a minuscula
print(animal.strip().capitalize()) #Quita espacios en blanco y pone primero mayuscula
print(animal.title()) #Cada inicio de palabra pone en mayuscula
print(animal.strip()) #
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("to"))
print(animal.replace("to", "tito"))
print("to" in animal)
print("to" not in animal)
print("a", "b", "c", sep="\n", end="...") #Sep es para separarlos de manera a como quieras, en este caso con un salto
#End es para hacer que termine en cierto formato, en este caso va a terminar en "..."
numero = 3
str(numero) #Hacer a string 

entrada = input("Dime algo: ") #Imput sirve para ingresar datos, todos los datos son de tipo "str"

#El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) 
#se convierte en un operador de replicación
"""Por ejemplo:

"James" * 3 produce "JamesJamesJames"
3 * "an" produce "ananan"
5 * "2" (o "2" * 5) produce "22222" (no 10!)
"""