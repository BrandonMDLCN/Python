"""
def es_palindromo(texto):
    pali = texto.lower().strip().replace(" ", "")
    tex = ""
    for pal in pali:
        tex += pal
    rev = tex[::-1]
    if rev == pali:
        return True
    else:
        return False


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("    Hola Mundo"))

"""

#Solucion en el video
def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_revez = reverse(texto)
    return texto.lower() == texto_al_revez.lower()


#es_palindromo("amo la paloma")    
es_palindromo("hola mundo")  