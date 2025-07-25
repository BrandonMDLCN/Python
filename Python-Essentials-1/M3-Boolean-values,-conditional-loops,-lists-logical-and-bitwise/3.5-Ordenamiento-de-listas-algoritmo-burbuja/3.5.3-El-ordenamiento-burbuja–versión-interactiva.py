"""
3.5.3 El ordenamiento burbuja – versión interactiva

En el editor, puedes ver un programa completo, enriquecido por una conversación con el usuario, y que permite ingresar e imprimir elementos de la lista: 
El ordenamiento burbuja - versión final interactiva.
"""

my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

"""
Python, sin embargo, tiene sus propios mecanismos de clasificación. 
Nadie necesita escribir sus propias clases, ya que hay un número suficiente de herramientas listas-para-usar.

Te explicamos este sistema de clasificación porque es importante aprender como procesar los contenidos de una lista y mostrarte como puede funcionar la clasificación real.

Si quieres que Python ordene tu lista, puedes hacerlo de la siguiente manera:
"""

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

"""
Es tan simple como eso.

La output del fragmento es la siguiente:

Output
[2, 4, 6, 8, 10]

Como puedes ver, todas las listas tienen un método denominado sort(), que las ordena lo más rápido posible. 
Ya has aprendido acerca de algunos de los métodos de lista anteriormente, y pronto aprenderás más sobre otros.
"""