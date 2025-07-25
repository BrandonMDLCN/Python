# Una tupla es una secuencia inmutable.

# las tuplas utilizan paréntesis, mientras que las listas usan corchetes, 
# aunque también es posible crear una tupla tan solo separando los valores por comas.
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
# Se definieron dos tuplas, ambas contienen cuatro elementos.

# A continuación se imprimen en consola:
print(tuple_1)
print(tuple_2)

# Nota: cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, o cualquier otro tipo de dato).

# ¿Es posible crear una tupla vacía? Si, solo se necesitan unos paréntesis:
empty_tuple = ()

# Si se desea crear una tupla de un solo elemento, se debe de considerar el hecho de que, 
# debido a la sintaxis (una tupla debe de poder distinguirse de un valor entero ordinario), se debe de colocar una coma al final:
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
#El quitar las comas no arruinará el programa en el sentido sintáctico, pero serán dos variables, no tuplas.

#Si deseas leer los elementos de una tupla, lo puedes hacer de la misma manera que se hace con las listas.
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# Todas estas instrucciones (con excepción de primera) causarán un error de ejecución:
my_tuple = (1, 10, 100, 1000)
 
"""my_tuple.append(10000)"""  # No debe ser tratado como una lista, marcará error
"""del my_tuple[0]"""
"""my_tuple[1] = -10"""

# ¿Qué más pueden hacer las tuplas?

# la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;
# el operador + puede unir tuplas (ya se ha mostrado esto antes)
# el operador * puede multiplicar las tuplas, así como las listas;
# los operadores in y not in funcionan de la misma manera que en las listas.
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))  # 9
print(t1)   # (1, 10, 100, 1000, 10000)
print(t2)   # (1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple) # True
print(-10 not in my_tuple) # True


# Observa el siguiente fragmento de código:

var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)
# Muestra tres tuplas interactuando - en efecto, los valores almacenados en ellas "circulan" entre ellas 
# - t1 se convierte en t2, t2 se convierte en t3, y t3 se convierte en t1.


"""
4.6.2 Tuples
The first and the clearest distinction between lists and tuples is the syntax used to create them - tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas.

Look at the example:


tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
There are two tuples, both containing four elements.

Let's print them:


tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
print(tuple_1)
print(tuple_2)
 
This is what you should see in the console:

Output
(1, 2, 4, 8)
(1.0, 0.5, 0.25, 0.125)
Note: each tuple element may be of a different type (floating-point, integer, or any other not-as-yet-introduced kind of data).

How to create a tuple
It is possible to create an empty tuple – parentheses are required then:


empty_tuple = ()
 
If you want to create a one-element tuple, you have to take into consideration the fact that, due to syntax reasons (a tuple has to be distinguishable from an ordinary, single value), you must end the value with a comma:

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
 
Removing the commas won't spoil the program in any syntactical sense, but you will instead get two single variables, not tuples.

How to use a tuple
If you want to get the elements of a tuple in order to read them over, you can use the same conventions to which you're accustomed while using lists.

Take a look at the code in the editor.

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

The program should produce the following output − run it and check:

Output
1
1000
(10, 100, 1000)
(1, 10)
1
10
100
1000
The similarities may be misleading − don't try to modify a tuple's contents! It's not a list!

All of these instructions (except the topmost one) will cause a runtime error:


my_tuple = (1, 10, 100, 1000)
 
my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10
 
This is the message that Python will give you in the console window:

Output
AttributeError: 'tuple' object has no attribute 'append'
What else can tuples do for you?

the len() function accepts tuples, and returns the number of elements contained inside;
the + operator can join tuples together (we've shown you this already)
the * operator can multiply tuples, just like lists;
the in and not in operators work in the same way as in lists.
The snippet in the editor presents them all.


my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


The output should look as follows:

Output
9
(1, 10, 100, 1000, 10000)
(1, 10, 100, 1, 10, 100, 1, 10, 100)
True
True
One of the most useful tuple properties is their ability to appear on the left side of the assignment operator. You saw this phenomenon some time ago, when it was necessary to find an elegant tool to swap two variables' values.

Take a look at the snippet below:


var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)
 
It shows three tuples interacting − in effect, the values stored in them "circulate" − t1 becomes t2, t2 becomes t3, and t3 becomes t1.

Note: the example presents one more important fact: a tuple's elements can be variables, not only literals. Moreover, they can be expressions if they're on the right side of the assignment operator.
"""