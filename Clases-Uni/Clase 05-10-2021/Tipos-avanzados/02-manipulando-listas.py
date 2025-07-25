mascotas = ["Wolfgang", "pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas)
print(mascotas[2:])
print(mascotas[-1])
print(mascotas[::2]) #toma el sigueinte, luego salto, el siguiente y luego salto

numeros = list(range(21))
print(numeros[::2]) #pares
print(numeros[1::2]) #inpares

value = 5
list.append(value)  #Un nuevo elemento puede ser añadido al final con el metodo append()
location = 0
list.insert(location, value) #insert(), es un poco mas inteligente
#puede agregar en cualquier lugar
#location, lugar donde se va a insertar (todos los elementos restantes se van a derecha)

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1 #permite intercambiar valores


#################################### 

my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0] #Intercambia el valor de las pocisiones
my_list[1], my_list[3] = my_list[3], my_list[1] #Intercambia el valor de las pocisiones
 
print(my_list)

for i in range(length // 2):    #ayuda con pares e impares, el del medio intacto
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)