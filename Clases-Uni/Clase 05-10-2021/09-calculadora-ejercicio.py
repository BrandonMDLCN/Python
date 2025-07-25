#"""
print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")
numero = 0
while True:
    if numero == 0:
        numero = input("Ingresa número: ")        
        if numero.lower() =="salir":
            break
    else:
        numero = int(numero)
        cal = input("Ingresa operación: ").lower()
        if cal.lower() == "salir":
            break
        numero2 = input("ingresa el siguiente numero: ").lower()
        if numero2 == "salir":
                break        
        numero2 = int(numero2)
        if cal.lower() == "suma":
            op = numero + numero2
        if cal.lower() == "multi":
            op = numero * numero2
        if cal.lower() == "div":
            op = numero / numero2
        if cal.lower() == "resta":
            op = numero - numero2
        print(op)
        numero = op





    """

print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")
resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() =="salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    elif op.lower() == "resta":
        resultado -= n2
    else:
        print("Operacion no valida")
        break
    print(f"El resultado es {resultado}")
    """