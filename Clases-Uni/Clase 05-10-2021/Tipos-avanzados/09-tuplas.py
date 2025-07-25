#Tupla es una lista pero no se puede modificar las ya existentes
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

puntos = tuple([1, 2])
print(puntos)
menosmumestos = numeros[:2]
print(menosmumestos)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

listanumeros = list(numeros)    #Hicimos una lista a aprtir de una tupla pero la tupla no se modifico
listanumeros[0] = "Chanchito feliz"
print(listanumeros)