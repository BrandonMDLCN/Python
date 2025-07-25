#and, or, not
gas = True
encendido = True
edad = 18

if not gas and (encendido or edad >17):
    print("Puedes avanzar")
    pass

#Operadores de bit
#   and == & (ampersand)    #Requiere exactamente dos 1
#   or == | (barra vertical)    #requiere al menos un 1
#   not == ~ (tilde)
#   xor == ^ (signo de intercalación)   #requiere exactamente un 1
    
    #Los operadores deben de ser enteros

#Desplazamiento binario (Toma el valor binario y lo desplaza)
var = 17
var_right = var >> 1 #Desplazamiento binario a la derecha (Basicamente 17 dividido entre 2 a la potencia 1)
var_left = var << 2 #Desplazamiento 2 binario a la izquierda (Basicamente 17 multiplicando por 2 a la potencia 2)
print(var, var_left, var_right)
