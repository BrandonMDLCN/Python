#set significagrupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
primer.add(5)
primer.remove(1)
segundo = [3, 4, 5]
segundo = set(segundo)  #hacemos un set a partir de una lista
print(primer)
print(segundo)
print(f"union | {primer | segundo}") #union
print( f"Interseccion & {primer & segundo}")    #interseccion   #Imprime los que estan en primero y segundo solamente
print(f"Diferencia - {primer - segundo}") #Diferencia #Quita elementos del primero que se encuentren en el segundo
print(f"Difernecia simetrica ^{primer ^segundo}")  #Diferencia simetrica   #los que se encuentren duplicados se van a eliminar

if 5 in segundo:
    print("Hola mundo")