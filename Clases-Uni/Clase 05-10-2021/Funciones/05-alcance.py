saludo = "Hola global"  #valiables globales es una MALA PRACTICA

def saludar():
    global saludo
    saludo = "Hola mundo"


def saludachanchito():
    saludo = "Hola chamchito"


