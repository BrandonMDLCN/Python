# 2.1.11 Argumentos de palabra clave

"""
Python ofrece otro mecanismo para el paso de argumentos, que puede ser útil cuando deseas convencer a la función print() para que cambie un poco su comportamiento.

No vamos a explicarlo en profundidad ahora. Planeamos hacerlo cuando hablemos de funciones. Por ahora, simplemente queremos mostrarte cómo funciona. Siéntete libre de usarlo en tus propios programas.

El mecanismo se llama argumentos de palabras clave. El nombre proviene del hecho de que el significado de estos argumentos se toma no de su ubicación (posición) sino de la palabra especial (palabra clave) utilizada para identificarlos.

La función print() tiene dos argumentos de palabra clave que puedes usar para tus propósitos. El primero se llama end.

En la ventana del editor puedes ver un ejemplo muy simple de cómo usar un argumento de palabra clave.
"""


print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")


"""
Para usarlo, es necesario conocer algunas reglas:

Un argumento de palabra clave consta de tres elementos: una palabra clave se identifica el argumento (end aquí); un signo de igual (=); y un valor asignado a ese argumento;
cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)
En nuestro ejemplo, hemos utilizado el argumento de palabra clave end, y lo hemos configurado como cadena que contiene un espacio.

Ejecuta el código para ver cómo funciona.

La consola ahora debería estar mostrando el siguiente texto:

Output
Mi nombre es Python. Monty Python.
Como puedes ver, el argumento de palabra clave end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales.

El comportamiento predeterminado refleja la situación en la que el argumento de palabra clave end se usa implícitamente de la siguiente manera: end="\n".

Y ahora es el momento de intentar algo más difícil.

Si miras con atención, verás que hemos usado el argumento end, pero la cadena que se le asignó está vacía (no contiene ningún carácter).

¿Qué sucederá ahora? Ejecuta el programa en el editor para averiguarlo.
"""

print("Mi nombre es ", end="")
print("Monty Python.")

"""
Como el argumento end se ha establecido a nada, la función print() tampoco genera nada, una vez que se han agotado sus argumentos posicionales.

La consola ahora debería mostrar el siguiente texto:

Output
Mi nombre es Monty Python.
Nota: no se han enviado líneas nuevas a la salida.

La cadena asignada al argumento de palabra clave end puede ser de cualquier longitud. Experimenta con él si quieres.

Dijimos anteriormente que la función print() separa sus argumentos de salida con espacios. Este comportamiento también se puede cambiar.

El argumento de palabra clave que puede hacer esto se denomina sep (como en separador).

Mira el código en el editor, y ejecútalo.
"""

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")


"""
El argumento sep produce los siguientes resultados:

Output
Mi-nombre-es-Monty-Python.
La función print() ahora usa un guión, en lugar de un espacio, para separar los argumentos de salida.

Nota: el valor del argumento sep también puede ser una cadena vacía. Pruébalo tu mismo.

Ambos argumentos de palabra clave pueden mezclarse en una invocación, como aquí en la ventana del editor.
"""


print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


"""
El ejemplo no tiene mucho sentido, pero presenta de forma visible las interacciones entre end y sep.

¿Puedes predecir el resultado?

Ejecuta el código y comprueba si coincide con tus predicciones.

Ahora que comprendes la función print(), estás listo para considerar cómo almacenar y procesar datos en Python.

Sin print(), no podrías ver ningún resultado.


"""