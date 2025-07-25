try:
	# Es un lugar donde
	# tu puedes hacer algo 
    # sin pedir permiso.
    pass
except:
	# Es un espacio dedicado  
    # exclusivamente para pedir perdón.
    pass

# Puedes ver dos bloques aquí:

# el primero, comienza con la palabra clave reservada try este es el lugar donde se coloca el código que se sospecha que es riesgoso y puede terminar en caso de un error; 
# nota: este tipo de error lleva por nombre excepción, mientras que la ocurrencia de la excepción se le denomina generar - podemos decir que se genera (o se generó) una excepción;

# el segundo, la parte del código que comienza con la palabra clave reservada except esta parte fue diseñada para manejar la excepción; 


# 4.7.4 La excepción confirma la regla
# Reescribamos el código para adoptar el enfoque de Python para la vida:
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)
