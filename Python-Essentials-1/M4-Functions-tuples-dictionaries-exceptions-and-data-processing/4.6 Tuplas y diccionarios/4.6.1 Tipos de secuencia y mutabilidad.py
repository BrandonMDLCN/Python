# 4.6.1 Tipos de secuencia y mutabilidad


# tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar más de un valor (o ninguno si la secuencia esta vacía), 
# los cuales pueden ser secuencialmente (de ahí el nombre) examinados, elemento por elemento.
# Es decir es iterable

# la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder cambiar libremente durante la ejecución de un programa.
# Existen dos tipos de datos en Python: mutables e inmutables.

# Los datos mutables pueden ser actualizados libremente en cualquier momento - a esta operación se le denomina "in situ".
# Una tupla es una secuencia inmutable.
# Se puede comportar como una lista pero no puede ser modificada en el momento.
# Si tienes los datos y quieres agregar uno mas, Se tendría que crear una lista completamente nueva, la cual contenga los elementos ya existentes más el nuevo elemento.

"""
4.6.1 Sequence types and mutability
Before we start talking about tuples and dictionaries, we have to introduce two important concepts: sequence types and mutability.

A sequence type is a type of data in Python which is able to store more than one value (or less than one, as a sequence may be empty), and these values can be sequentially (hence the name) browsed, element by element.

As the for loop is a tool especially designed to iterate through sequences, we can express the definition as: a sequence is data which can be scanned by the for loop.

You've encountered one Python sequence so far − the list. The list is a classic example of a Python sequence, although there are some other sequences worth mentioning, and we're going to present them to you now.

The second notion − mutability − is a property of any Python data that describes its readiness to be freely changed during program execution. There are two kinds of Python data: mutable and immutable.

Mutable data can be freely updated at any time − we call such an operation in situ.

In situ is a Latin phrase that translates as literally in position. For example, the following instruction modifies the data in situ:


list.append(1)
 
Immutable data cannot be modified in this way.

Imagine that a list can only be assigned and read over. You would be able neither to append an element to it, nor remove any element from it. This means that appending an element to the end of the list would require the recreation of the list from scratch.

You would have to build a completely new list, consisting of the all elements of the already existing list, plus the new element.

The data type we want to tell you about now is a tuple. A tuple is an immutable sequence type. It can behave like a list, but it can't be modified in situ.
"""