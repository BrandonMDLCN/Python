# El método keys()
# La propiedad keys() es una función que devuelve un array de las claves (o indices) del objeto.

# ¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas? No y si.
# No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.
# Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a los requerimientos del bucle for (Un enlace intermedio).
# El método keys() retorna o regresa una lista de todas las claves dentro del diccionario.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key]);

# Otra manera de hacerlo es utilizar el método items().
# retorna una lista de tuplas (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) donde cada tupla es un par de cada clave con su valor.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french);

# Modificar, agregar y eliminar valores
print("Modificar, agregar y eliminar valores")
# El asignar un nuevo valor a una clave existente es sencillo - debido a que los diccionarios son completamente mutables, no existen obstáculos para modificarlos.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)

# La función sorted(), ordena el diccionario
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key]);



# También existe un método denominado values()
print("values()")
# funciona de manera muy similar al de keys(), pero regresa una lista de valores.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for french in dictionary.values():
    print(french);

# Agregando nuevas claves
print("Agregando nuevas claves")
# se tiene que asignar un valor a una nueva clave que no haya existido antes.
# A continuación se agrega un par nuevo al diccionario - un poco extraño pero válido:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne'
print(dictionary)

# Eliminado una clave
print("Eliminado una clave")
# al eliminar la clave también se removerá el valor asociado. 
# Los valores no pueden existir sin sus claves.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)
# el eliminar una clave no existente, provocará un error.

# Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem():
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.popitem()
print(dictionary) # salida: {'gato': 'chat', 'perro': 'chien'}


"""
4.6.4 Dictionary methods and functions
The keys() method
Can dictionaries be browsed using the for loop, like lists or tuples?

No and yes.

No, because a dictionary is not a sequence type − the for loop is useless with it.

Yes, because there are simple and very effective tools that can adapt any dictionary to the for loop requirements (in other words, building an intermediate link between the dictionary and a temporary sequence entity).

The first of them is a method named keys(), possessed by each dictionary. The method returns an iterable object consisting of all the keys gathered within the dictionary. Having a group of keys enables you to access the whole dictionary in an easy and handy way.

Just like here:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
 
The code's output looks as follows:

Output
horse -> cheval
dog -> chien
cat -> chat
Let's now have a look at a dictionary method called items(). The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair.

This is how it works:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for english, french in dictionary.items():
    print(english, "->", french)
 
Note the way in which the tuple has been used as a for loop variable.

The example prints:

Output
cat -> chat
dog -> chien
horse -> cheval
Modifying and adding values
Assigning a new value to an existing key is simple - as dictionaries are fully mutable, there are no obstacles to modifying them.

We're going to replace the value "chat" with "minou", which is not very accurate, but it will work well with our example.

Look:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary['cat'] = 'minou'
print(dictionary)
 
The output is:

Output
{'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}
Do you want it sorted? Just enrich the for loop to get such a form:


for key in sorted(dictionary.keys()):
There is also a method called values(), which works similarly to keys(), but returns values.

Here is a simple example:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for french in dictionary.values():
    print(french)
 
As the dictionary is not able to automatically find a key for a given value, the role of this method is rather limited.

Adding a new key
Adding a new key-value pair to a dictionary is as simple as changing a value – you only have to assign a value to a new, previously non-existent key.

Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.

Let's add a new pair of words to the dictionary − a bit weird, but still valid:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary['swan'] = 'cygne'
print(dictionary)
 
The example outputs:

Output
{'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}
  Note  
You can also insert an item to a dictionary by using the update() method, e.g.:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary.update({"duck": "canard"})
print(dictionary)
 
Removing a key
Can you guess how to remove a key from a dictionary?

Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys.

This is done with the del instruction.

Here's the example:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
del dictionary['dog']
print(dictionary)
 
Note: removing a non-existing key causes an error.

The example outputs:

Output
{'cat': 'chat', 'horse': 'cheval'}
  EXTRA  
To remove the last item in a dictionary, you can use the popitem() method:


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary.popitem()
print(dictionary) # outputs: {'cat': 'chat', 'dog': 'chien'}
 
In the older versions of Python, i.e., before 3.6.7, the popitem() method removes a random item from a dictionary.
"""