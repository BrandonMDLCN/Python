# la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
# el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
# el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
# todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
# el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
# el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
# la maquina responde con su movimiento y se verifica el estado del juego;
# no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

from random import randrange


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    a = "+-------+-------+-------+"
    b = "|       |       |       |"
    print(a,b, sep="\n")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print(b,a,b, sep="\n")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print(b,a,b, sep="\n")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print(b,a, sep="\n")
    pass 

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    sign = "O"
    O = int(input("Ingresa tu movimiento: "))
    if O > 0 and O < 10:
        if O == 1:
            if board[0][0] == "O" or board[0][0] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[0][0] = "O"
        elif O == 2:
            if board[0][1] == "O" or board[0][1] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[0][1] = "O"
        elif O == 3:
            if board[0][2] == "O" or board[0][2] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[0][2] = "O"
        elif O == 4:
            if board[1][0] == "O" or board[1][0] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[1][0] = "O"
        elif O == 6:
            if board[1][2] == "O" or board[1][2] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[1][2] = "O"
        elif O == 7:
            if board[2][0] == "O" or board[2][0] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[2][0] = "O"
        elif O == 8:
            if board[2][1] == "O" or board[2][1] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[2][1] = "O"
        elif O == 9:
            if board[2][2] == "O" or board[2][2] == "X":
                print("Casilla ocupado")
                enter_move(board)
            else:                
                board[2][2] = "O"
        display_board(board)
    else:
        return "Invalid move!"
    victory_for(board, sign)    
    return turno_de_X(board, make_list_of_free_fields(board))

def turno_de_X(board, free_fields):
    sign = "X"
    if len(free_fields) == 0:   
        return victory_for(board, sign)
    else:
        X = free_fields[randrange(len(free_fields))]
        board[X[0]][X[1]] = "X"
        free_fields.remove(X)
        display_board(board)
        print("Casillas disponibles: " , free_fields)
        return enter_move(board)
    

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    # La función retorna una lista de tuplas vacías.    
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != "X" and board[i][j] != "O":
                free_fields.append((i,j));
    return free_fields


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if board[0]  == [sign]*3:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!")
    elif board[1]  == [sign]*3:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!")
    elif board[2]  == [sign]*3:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!")
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!")
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!")
    elif board[0][2] == sign and board[1][2] == sign and board[1][2] == sign:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!")
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!")
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        if sign=="X":
            return print("Yo gano!")
        else:
            return print("Tu ganas!") 
    elif len(make_list_of_free_fields(board)) == 0:          
        return draw_move(board)
    pass

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    board = [[1,2,3], [4,"X",6], [7,8,9]]
    print("Empate")
    return display_board(board)

board = [[1,2,3], [4,"X",6], [7,8,9]]
display_board(board)
enter_move(board)


#-------------------------------------------------------------------#

#Soloción de Cisco
from random import randrange


def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
	ok = False	# suposición falsa - la necesitamos para entrar en el bucle
	while not ok:
		move = input("Ingresa tu movimiento: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # ¿es valido lo que ingreso el usuario?
		if not ok:
			print("Movimiento erróneo, ingrésalo nuevamente") # no, no lo es. ingrésalo nuevamente
			continue
		move = int(move) - 1 	# numero de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X'] 
		if not ok:	# esta ocupado, ingresa una posición nuevamente
			print("¡Cuadro ocupado, ingresa nuevamente!")
			continue
	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado


def make_list_of_free_fields(board):
	free = []	# la lista esta vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # iitera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # si, agrega una nueva tupla a la lista
	return free


def victory_for(board,sgn):
	if sgn == "X":	# ¿Estamos buscando X?
		who = 'me'	# Si, es la maquina
	elif sgn == "O": # ... ¿o estamos buscando O?
		who = 'you'	# Si, es el usuario
	else:
		who = None	# ¡No debemos de caer aquí!
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # revisar la primer diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board) # crea una lista de los cuadros vacios o libres
	cnt = len(free)
	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primer 'X' en el centro
free = make_list_of_free_fields(board)
human_turn = True # ¿De quien es turno ahora?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("¡Has ganado!")
elif victor == 'me':
	print("¡He ganado!")
else:
	print("¡Empate!")