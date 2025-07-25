punto = {"x": 25, "y": 50}  #izquierda son puros string, derecha cualquier cosa
print(punto)
print(punto["x"])   #Para acceder a un diccionario es necesario pasarle el argumento
print(punto["y"])

punto["z"] = 45
#print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)    #Devuelve tuplas

for llave, valor in punto.items():
    print(llave, valor)    #Desempaquetando tuplas


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]    

for usuario in usuarios:
    print(usuario["nombre"])