# Escribamos un fragmento de código extremadamente trivial - leerá un número natural (un entero no negativo) e imprimirá su recíproco. 
# De esta forma, 2 se convertirá en 0.5 (1/2) y 4 en 0.25 (1/4). Aquí está el programa:
value = int(input('Ingresa un número natural: '))
print('El recíproco de', value, 'es', 1/value)

# ngresar datos que no sean un número entero (que también incluye ingresar nada) arruinará completamente la ejecución del programa.

#puedes validar el tipo de dato para detener antes de ejecutar
type(value) is int
# aunque python no recomienda esta forma