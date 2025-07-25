numeros = [1, 2, 3]   #[inicia lista, 2, termina elemento de lista]
print(sum(numeros)) #Suma elementos iterables
letras = ["a", "b", "c"]
palabras = ["chanchito", "feliz"]
palabrasfelices = ["chanchito", "feliz", "Felipe", "alumno"]
booleans = [True, False, True, True]
matriz = [[0,1], [1,0]]
ceros = [0] * 10
alfanumericos = numeros + letras
rango = list(range(1,11))
chars = list("hola mundo")
print(chars)

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111 #Asignación de otro valor
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  
# Imprimiendo el contenido de la lista actual.

print("\nLongitud de la lista:", len(numbers))  
# len permite imprimir la longitud de la lista.

del numbers[1]  # del es una instruccion que elimina elemento apuntado de la lista.
print("Longitud de la nueva lista:", len(numbers))  
# Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  
# Imprimiendo el contenido de la lista actual.

numbers = [111, 7, 2, 1]
print(numbers[-1]) #El indice -1 es el ultimo en la lista
print(numbers[-2]) #El indice -2 es el penultimo en la lista