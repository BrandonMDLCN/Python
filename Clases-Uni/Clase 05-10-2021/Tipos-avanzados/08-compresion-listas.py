usuarios = [
    ["Chancito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
    ]

nombres = []
for ususario in usuarios:
    nombres.append(ususario[0])
print(nombres)    
  # nombres = [expresion for item in items]
# Modificar elementos    #map
nombres = [ususario[0] for ususario in usuarios]
# filtrar    #filter
nombres = [ususario for ususario in usuarios if ususario[1] > 2]
# Filtrar y transformar
nombres = [ususario[0] for ususario in usuarios if ususario[1] > 2]

nombres = list(map(lambda ususario: ususario[0], usuarios))

menosususarios = list(filter(lambda ususario: ususario[1] > 2, usuarios))
print(nombres)
print(menosususarios)


###########################

list_1 = [1] #Lista almacena 1
list_2 = list_1 #lista 2 = lista 1
list_1[0] = 2 #modificas lista 1
print(list_2) #Output: [2]
#Esto se debe a que no se esta copeando el contenido de la lista, si no el nombre (Ubiacacion de la memoria)

#la solución, se llama rebanada
#Permite hacer una copia nueva de una lista, o partes de una lista
#Copia el contenido, no el nombre
list_1 = [1]
list_2 = list_1[:]  #my_list[inicio:fin-1] desde el inicio pero uno antes del fin
list_1[0] = 2
print(list_2)

#########################

my_list = [0, 3, 12, 8, 2]

print(5 in my_list) #in devuelve False, ya que no esta dentro de la lista
print(5 not in my_list) #not in devuelve True, ya que realmente no esta dentro de la lista
print(12 in my_list)  #in devuelve True, ya que si esta dentro de la lista