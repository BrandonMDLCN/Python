numeros = [2, 4, 1, 45, 75, 22]

numeros.sort(reverse=True)  #Ordena la misma lista
numeros2 = sorted(numeros, reverse=True) #hace una nueva lista
print(numeros)
print(numeros2)

numeros.reverse()   #Invierte la lista
print(numeros)

usuarios = [
    ["Chancito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
    ]
#Funcion 1 sola ves no hay problemas en utilizar lambdas
usuarios.sort(key=lambda elemen: elemen[1])  #Funciones anonimas, lambda parametros : valor retorno
print(usuarios)

####################

#Ordenamiento Metodo Burbuja
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
 
for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
 

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)