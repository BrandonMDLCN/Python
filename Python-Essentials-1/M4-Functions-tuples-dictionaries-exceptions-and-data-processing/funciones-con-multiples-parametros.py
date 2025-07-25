#Calculadora de IMC
def bmi(weight, height):
    return weight / height ** 2
 
 
print(bmi(52.5, 1.65))

# Ejemplos de funciones: Triángulos
# La suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

#----------------------------------------------------------------#
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')

# Ejemplos de funciones: Factoriales
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # probando
    print(n, factorial_function(n))

# Números Fibonacci
    # el primer elemento de la secuencia es igual a uno (Fib1 = 1)
    # el segundo elemento también es igual a uno (Fib2 = 1)
    # cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # probando
    print(n, "->", fib(n))

#----------------------------------------------------------------#
# Recursividad
# Cuando una función se invoca a si misma, se le conoce como recursividad, y la función que se invoca a si misma 
# y contiene una condición de terminación es llamada una función recursiva.
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))

# Implementación recursiva de la función factorial.
 
def factorial(n):
    if n == 1: # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24

