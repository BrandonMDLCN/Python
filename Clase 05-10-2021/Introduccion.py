#aqui se define la clase
class Persona:
    
    #atributos de la clase
    nombre = ''
    edad = 0
    estatura = 0
    peso = 0
    
    #definir metodo con 2 parametros
    def persona_ratio(self, edad, peso):
        P_ratio = edad / peso #realizamos una operacion
        return P_ratio #retornamos el resultado del metodo
    
#aqui definimos la instancia/herencia    
persona_1 = Persona() 

#asignacion de valores a los atributos
persona_1.nombre='carlos'
persona_1.edad = 32
persona_1.estatura = 1.82
persona_1.peso = 74

#aqui definimos la segunda instancia/herencia 
persona_2 = Persona() 

#asignacion de valores a los atributos
persona_2.nombre='Angela'
persona_2.edad = 28
persona_2.estatura = 1.70
persona_2.peso = 72

#realiza operaciones
nueva_persona =persona_1.nombre + ' ' + persona_2.nombre
edad_diferencia = persona_1.edad - persona_2.edad
est_diff = persona_1.estatura - persona_2.estatura
peso_ambos = persona_1.peso + persona_2.peso

#aqui utilizamos o mandamos a llamar el metodo
persona1_met =persona_1.persona_ratio(persona_1.edad, persona_1.peso)

persona2_met = persona_1.persona_ratio(persona_2.edad, persona_2.peso)


















