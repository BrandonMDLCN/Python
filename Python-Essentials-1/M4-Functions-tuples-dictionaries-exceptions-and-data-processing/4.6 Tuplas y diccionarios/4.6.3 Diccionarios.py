# El diccionario es otro tipo de estructura de datos de Python. 
# No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.

# Si deseas asignar algunos pares iniciales a un diccionario, utiliza la siguiente sintaxis:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# La lista de todos los pares es encerrada con llaves, mientras que los pares son separados por comas, y las claves y valores por dos puntos.

# la palabra que se esta buscando se denomina key (clave). La palabra que se obtiene del diccionario es denominada value (valor).
# Esto significa que un diccionario es un conjunto de pares de key y value.

#Nota:
# cada clave debe de ser única - no es posible tener una clave duplicada;
# una clave puede ser un de dato de cualquier tipo - puede ser un número (entero o flotante), incluso una cadena, pero NO una LISTA;
# un diccionario NO es una LISTA - una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores;
# la función len() aplica también para los diccionarios - regresa la cantidad de pares (clave-valor) en el diccionario;
# un diccionario es una herramienta de un solo sentido 
#- si fuese un diccionario español-francés, podríamos buscar en español para encontrar su contraparte en francés más no viceversa.


# Si deseas obtener cualquiera de los valores, debes de proporcionar una clave válida:
print(dictionary['gato'])
print(phone_numbers['Suzy'])
# El obtener el valor de un diccionario es semejante a la indexación, gracias a los corchetes alrededor del valor de la clave.
# Nota:
# si una clave es una cadena, se tiene que especificar como una cadena;
# las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.


#No se puede utilizar una clave que no exista. 
# existe una manera simple de evitar dicha situación. El operador in, junto con su acompañante, not in

# El siguiente código busca de manera segura palabras en francés:

dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario");

# Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# Escribe un programa que convierta la tupla colors en un diccionario.
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

"""
4.6.3 Dictionaries
The dictionary is another Python data structure. It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.

To explain what the Python dictionary actually is, it is important to understand that it is literally a dictionary.


How to make a dictionary
If you want to assign some initial pairs to a dictionary, you should use the following syntax:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
 
In the first example, the dictionary uses keys and values which are both strings. In the second one, the keys are strings, but the values are integers. The reverse layout (keys → numbers, values → strings) is also possible, as well as number-number combinations.

The list of pairs is surrounded by curly braces, while the pairs themselves are separated by commas, and the keys and values by colons.

The first of our dictionaries is a very simple English-French dictionary. The second − a very tiny telephone directory.

The empty dictionary is constructed by an empty pair of curly braces − nothing unusual.

The Python dictionary works in the same way as a bilingual dictionary. For example, you have an English word (e.g., cat) and need its French equivalent. You browse the dictionary in order to find the word (you may use different techniques to do that − it doesn't matter) and eventually you get it. Next, you check the French counterpart and it is (most probably) the word "chat".

In Python's world, the word you look for is named a key. The word you get from the dictionary is called a value.

This means that a dictionary is a set of key-value pairs. Note:

each key must be unique − it's not possible to have more than one key of the same value;
a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
a dictionary is not a list − a list contains a set of numbered values, while a dictionary holds pairs of values;
the len() function works for dictionaries, too − it returns the number of key-value elements in the dictionary;
a dictionary is a one-way tool − if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.
Now we can show you some working examples.

The dictionary as a whole can be printed with a single print() invocation. The snippet may produce the following output:

Output
{'dog': 'chien', 'horse': 'cheval', 'cat': 'chat'}
{'Suzy': 5557654321, 'boss': 5551234567}
{}
Have you noticed anything surprising? The order of the printed pairs is different than in the initial assignment. What does that mean?

First of all, it's a confirmation that dictionaries are not lists - they don't preserve the order of their data, as the order is completely meaningless (unlike in real, paper dictionaries). The order in which a dictionary stores its data is completely out of your control, and your expectations. That's normal. (*)

  Note  
(*) In Python 3.6x dictionaries have become ordered collections by default. Your results may vary depending on what Python version you're using.

How to use a dictionary
Analyze the code in the editor:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Print the values here.

If you want to get any of the values, you have to deliver a valid key value:


print(dictionary['cat'])
print(phone_numbers['Suzy'])
 
Getting a dictionary's value resembles indexing, especially thanks to the brackets surrounding the key's value.

Note:

if the key is a string, you have to specify it as a string;
keys are case-sensitive: 'Suzy' is something different from 'suzy'.
The snippet outputs two lines of text:

Output
chat
22657854310
And now the most important news: you mustn't use a non-existent key. Trying something like this:


print(phone_numbers['president'])
 
will cause a runtime error. Try to do it.

Fortunately, there's a simple way to avoid such a situation. The in operator, together with its companion, not in, can salvage this situation.

The following code safely searches for some French words:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
 
The code's output looks as follows:

Output
cat -> chat
lion is not in dictionary
horse -> cheval
  Note  
When you write a big or lengthy expression, it may be a good idea to keep it vertically aligned. This is how you can make your code more readable and more programmer-friendly, e.g.:


# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}
 
This kind of formatting is called a hanging indent.
"""