# Dos excepciones después de un try

# Observa el código en el editor. Como puedes ver, acabamos de agregar un segundo except.
# si se ejecuta una, todas las demás permanecen inactivas.
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.');

# la cantidad de except no está limitada - puedes especificar tantas o tan pocas como necesites, 
# pero no se te olvide que ninguna de las excepciones se puede especificar más de una vez.
    
# 4.7.6 La excepción predeterminada y cómo usarla
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    ('No se que hacer con.')    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!');
# Hemos agregado un tercer except, pero esta vez no tiene un nombre de excepción específico 
# – podemos decir que es anónimo o (lo que está más cerca de su función real) es el por defecto.

# Puedes esperar que cuando se genere una excepción y no haya un except dedicado a esa excepción, esta será manejada por la excepción por defecto.