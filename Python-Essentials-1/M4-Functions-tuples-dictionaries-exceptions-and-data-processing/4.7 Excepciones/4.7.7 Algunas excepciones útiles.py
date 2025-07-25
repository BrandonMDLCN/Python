# ZeroDivisionError
# cuando intentas forzar a Python a realizar cualquier operación que provoque una división en la que el divisor es cero o no se puede distinguir de cero.

# ValueError
# excepción cuando estás manejando valores que pueden usarse de manera inapropiada en algún contexto.
# se genera cuando una función (como int() o float()) recibe un argumento de un tipo adecuado, pero su valor es inaceptable.

# TypeError
# Esta excepción aparece cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual.
short_list = [1]
one_value = short_list[0.5]
# No está permitido usar un valor flotante como índice de una lista (la misma regla también se aplica a las tuplas).

# AttributeError
# cuando intentas activar un método que no existe en un elemento con el que se está tratando.
short_list = [1]
short_list.append(2)
short_list.depend(3)
# La tercera línea de nuestro ejemplo intenta hacer uso de un método que no está incluido en las listas.

# SyntaxError
# se genera cuando el control llega a una línea de código que viola la gramática de Python.
print("Hello" 1 "World")
# El error de syntaxis aquí es porque falta un espacio entre los dos argumentos del print, por lo tanto Python esperaba
# El error indica que hay un número entero donde debe haber una cadena, lo cual es incorrecto en este caso.

# IndexError
# Se produce si intentamos acceder a un índice de lista o a otro contenedor indexable que carece del elemento solicitado por ese índice.
# Se produce cuando intentas acceder a un índice de lista o a otro contenedor indexable que carece del elemento
# Se produce si se accede a un índice de lista o secuencia que no existe.
empty_list = []
try:
    value = empty_list[0]
except IndexError as e:
    print('Caught an exception!')
    print('The error is: %s' % e)

# KeyError
# Es similar al IndexError pero se lanza para situaciones en las que se busca un valor en un diccionario y no se
# Es similar al IndexError pero para diccionarios y conjuntos.
my_dict = {'key': 'value'}
try:
    value = my_dict['bad key']
except KeyError as e:
    print('Caught another exception!')
    print('The error is:', e)

# MemoryError
# Excepción que se lanza cuando no hay suficiente memoria RAM disponible para realizar una operación. Esto sucede generalmente porque ha hab
# Excepción que se lanza cuando no hay memoria suficiente para realizar una operación. Esto sucede generalmente porque ha habido una fuga de mem
# Excepción que se lanza cuando no hay memoria suficiente para realizar una operación. Esto sucede por dos razones principales:
# Excepción que se lanza cuando no hay memoria suficiente para realizar una operación. Esto sucede por dos razones: