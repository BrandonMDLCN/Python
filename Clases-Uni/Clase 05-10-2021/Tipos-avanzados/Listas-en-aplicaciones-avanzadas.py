#Listas dentro de listas, es como una fila del ajedres, tiene letras y numeros
row = []
 
for i in range(8):
    row.append("WHITE_PAWN")

#Comprensión de lsitas (Sirve para rellenar lsitas masivas)
#Es en realidad una lista pero se creo sobre la marcha, no se describe de forma estatica
row2 = ["WHITE_PAWN" for i in range(8)]
 
squares = [x ** 2 for x in range(10)] #Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

twos = [2 ** i for i in range(8)]   #Output: [1, 2, 4, 8, 16, 32, 64, 128]

odds = [x for x in squares if x % 2 != 0 ]  #lista solo los elementos impares de la lista squares

#Arreglos de dos dimensiones
board = []
 
for i in range(8):
    row = ["EMPTY" for i in range(8)]   #Crea lista con 8 EMPTY
    board.append(row)   #Asigna la lista anterior a lista board

#Se puede traducir o acortar anidandolo
board2 = [["EMPTY" for i in range(8)] for j in range(8)]
#La parte interna crea una fila, y la parte externa crea una lista de filas.
print(board2)
board2[0][0] = 2
board2[0][7] = 2
board2[7][0] = 2
board2[7][7] = 2
board2[4][2] = 3
board2[3][4] = 4
print(board2)

#########################
##  Aplicación  ##
#Temperatura por hora en un mes
temps = [[0.0 for h in range(24)] for d in range(31)] #Horas y dias
#
# La matriz se actualiza aquí.
#
 
total = 0.0
 
for day in temps:   #Va por dias
    total += day[11]    #Toma el valor de medio dia y lo suma
 
average = total / 31    #Saca el promedio
 
print("Temperatura promedio al mediodía:", average)

#########################
##  Aplicación  ##
#Temperatura mas alta en todo el mes

temps = [[0.0 for h in range(24)] for d in range(31)]   #Horas y dias
#
# La matriz se actualiza aquí.
#
 
highest = -100.0
 
for day in temps:   #Itera en todas las filas de la matriz temps
    for temp in day:    #Itera a través de todas las mediciones tomadas en un dia
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)

#Ahora cuenta los dias en que la temperatura al mediodía fue de al menos 20c
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "fueron los días calurosos.")