numero = 1
while numero < 100:
    print(numero)
    numero *= 2

comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

#Loop Infinitos    

comando = ""
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break #Siempre debe llevar un break para que no se trabe la computadora