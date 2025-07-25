mascotas = [
    "Wolfgang", 
    "Pelusa", 
    "Pulga", 
    "Felipe", 
    "Pulga", 
    "Chanchito feliz"
    ]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")

mascotas.remove("Pulga") #no va el indice, va el elemento  #Elimia el primero
mascotas.pop(1) #Quita elemento por el indice o el ultimo si no tiene argumento
del mascotas[0] #Quita de acuerdo al indice
mascotas.clear()
print(mascotas)