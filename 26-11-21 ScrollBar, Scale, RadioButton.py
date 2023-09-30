# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 11:16:22 2021

@author: BrandonDLC
"""

from tkinter import *

ventana_principal = Tk()
ventana_principal.geometry("300x350")

var1 = StringVar()

mensaje1 = Message(ventana_principal, textvariable = var1, relief = RAISED) #relief = FLAT

var1.set("Hola, buenos dias clase de 10 a 11 como estan?")

mensaje1.pack()
ventana_principal.mainloop()

#%%

#RADIO BUTTON

from tkinter import *

def sel():
    seleccion = "Tu has seleccionado la opcion: " + str(var1.get())
    etiqueta2.config(text = seleccion)
    
ventana_principal = Tk()
ventana_principal.geometry("330x150")

etiqueta1 = Label(text = "Lenguaje de Programacion Favorito:")
etiqueta1.pack()

var1 = IntVar()

RB1 = Radiobutton(ventana_principal, text = "Opcion 1", variable = var1, value = 1, command = sel)
RB1.pack(anchor = W)
RB2 = Radiobutton(ventana_principal, text = "Opcion 2", variable = var1, value = 2, command = sel)
RB2.pack(anchor = W)
RB3 = Radiobutton(ventana_principal, text = "Opcion 3", variable = var1, value = 3, command = sel)
RB3.pack(anchor = W)

etiqueta2 = Label(ventana_principal)
etiqueta2.pack()

ventana_principal.mainloop()

#%%

#SCALE

#Opciones:

#tickinterval = Intervalos en los que se muestran los valores
# resolution = Intervalos de cambio entre los valores

from tkinter import *

def sel():
    selc = "Valor = " +str(var1.get())
    etiqueta1.config(text = selc)
    
ventana_principal = Tk()
ventana_principal.geometry("200x100")

var1 = DoubleVar()

BE1 = Scale(ventana_principal, variable = var1, from_ = 1, to = 50, orient = HORIZONTAL)
BE1.pack(anchor = CENTER)

boton1 = Button(ventana_principal, text = "Valor", command = sel)
boton1.pack(anchor = CENTER)

etiqueta1 = Label(ventana_principal)
etiqueta1.pack()

ventana_principal.mainloop()

#%%

#SCROLL BAR

#Opciones:
    
# orient = Posicion del elemento o la forma en que lo necesites trabajar
        #VERTICAL y HORIZONTAL
        
#EJEMPLO: VERTICAL

from tkinter import *

ventana_principal = Tk()

SB1 = Scrollbar(ventana_principal)
SB1.pack(side = RIGHT, fill = Y)

LB1 = Listbox(ventana_principal, yscrollcommand = SB1.set)

for linea in range(30):
    LB1.insert(END, "Numero " + str(linea))
    
LB1.pack(side = LEFT)
SB1.config(command = LB1.yview) #see muestra la barra o se active

ventana_principal.mainloop()

#%%

#EJEMPLO 2: HORIZONTAL

from tkinter import *

ventana_principal = Tk()

SB1 = Scrollbar(ventana_principal, orient = HORIZONTAL)
SB1.pack(side = BOTTOM, fill = X)

LB1 = Listbox(ventana_principal, xscrollcommand = SB1.set)

for linea in range(30):
    LB1.insert(END, "Esta es el orden del elemento de la lista " + str(linea))
    
LB1.pack(side = LEFT)
SB1.config(command = LB1.xview) #see muestra la barra o se active

ventana_principal.mainloop()
































