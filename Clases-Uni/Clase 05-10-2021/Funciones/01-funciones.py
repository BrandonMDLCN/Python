def hola(nombre, apellido = "Feliz"):  #Parametros de la funcion (apellido tiene de manera predeterminada "Feliz")
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")   #Uso de sus parametros

#Una función y una variable no pueden compartir el mismo nombre.
def message():
    print("Ingresar valor: ")
 
message = 1 #Si lo ejecutas saldra error, python olvida el rol de la funcion

hola("Nicolas", "Shuurmann")    #Argumentos de la funcion
hola("Chanchito")


hola(apellido="Schurmann", nombre="Wolfgang")   #Puedes asignarle manualmente los argumentos a los parametros

# Recuerda: especificar uno o más parámetros en la definición de la función es un requerimiento, y 
# se debe de cumplir durante la invocación de la misma. Se debe proveer el mismo número de 
# argumentos como haya parámetros definidos.
def my_function(a, b, c):
    print(a, b, c)
 
my_function(1, 2, 3)


####################################
def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

######

def my_function():
    var = 2
    print("¿Conozco a la variable?", var)
 
 
var = 1
my_function()
print(var)

#Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, excluyendo a aquellas que tienen el mismo nombre.

######

def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)

#la palabra reservada "global" extiende el alcance de una variable incluyendo el cuerpo de las funciones