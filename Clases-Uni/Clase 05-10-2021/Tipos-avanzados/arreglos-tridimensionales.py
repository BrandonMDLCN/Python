#Imagina un hotel, 3 edificios, 15 pisos cada uno, 20 habitaciones por piso

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

#El primer índice (0 a 2) selecciona uno de los edificios; 
#el segundo (0 a 14) selecciona el piso, 
#el tercero (0 a 19) selecciona el número de habitación. 

rooms[1][9][13] = True  #Ocupa habitacion, segundo edificio, decimo piso, habitacion 14

rooms[0][4][1] = False  #Desocupa segundo cuarto en el quinto piso en primer edificio

#Verifica si hay disponibilidad en el piso 15 del tercer edificio
vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)
 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)'

# Cubo - un arreglo tridimensional (3x3x3)
 
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'        