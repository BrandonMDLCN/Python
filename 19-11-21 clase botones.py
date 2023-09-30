# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:33:11 2021

@author: BrandonDLC
"""
#Softwares para programar visualmente
#Tkinter, wxPython y JPython

#BUTTON:
    
#Opciones:
    
# activebackground = Color de fondo del boton al momento de hacer click
# activeforeground = Color del texto al hacer click
# bg = Color de fondo del boton
# command = Llama la funcion que representa la accion que realizara el boton
# fg = Cabias el color del texto
# font = El tipo de letra
# text = Insertas un texto en el boton
# height = Cambias la altura del boton
# width = Cambias el ancho del boton
# image = Inserta una imagen en el boton
# state = Cambiar el estado del boton [activated] o [disabled]

from tkinter import *

ventana_principal = Tk()

ventana_principal.geometry("300x300")
#todos los elementos o controles de GUI que vamos a necesitar
def activo():
    print("Boton presionado")
    
    
boton1 = Button(ventana_principal, text = "Rojo", fg = "red", activebackground = "blue", command = lambda:activo(1))
boton2 = Button(ventana_principal, text = "Negro", fg = "black")
boton3 = Button(ventana_principal, text = "Verde", fg = "green")

if boton1 == 1:
    a = 1
    print("Boton si")
    
else:
    a = 0
#Formas de organizar elementos
#No se pueden mezclar formas de organizar elementos
#boton1.pack(side = LEFT)  #organizacion sea por bloques
#boton2.pack(side = RIGHT)
#boton3.pack(side = BOTTOM)

#Organizacion por cuadricula o tabla
#boton1.grid(row = 0, column = 1)
#boton2.grid(row = 0, column = 2)
#boton2.grid(row = 1, column = 2)

#Organizacion por coordenadas y puntos
boton1.place(x = 10, y = 10)
boton2.place(x = 100, y = 10)
boton3.place(x = 100, y = 150)

ventana_principal.mainloop()








