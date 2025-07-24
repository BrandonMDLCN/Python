# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:20:49 2021

@author: BrandonDLC
"""

#ENTRY

from tkinter import *

ventana_principal = Tk()
ventana_principal.geometry("400x250")

nombre = Label(ventana_principal, text = "Nombre").place(x = 30, y = 50)
correoe = Label(ventana_principal, text = "E-Mail").place(x = 30, y = 90)
contra = Label(ventana_principal, text = "PassW").place(x = 30, y = 130)

boton1 = Button(ventana_principal, text = "Iniciar", activebackground = "green", activeforeground = "red").place(x = 30, y = 170)

e1 = Entry(ventana_principal, font = "Helvetica 10").place(x = 90, y = 50)
e2 = Entry(ventana_principal, font = "Helvetica 10").place(x = 90, y = 90)
e3 = Entry(ventana_principal, font = "Helvetica 10").place(x = 90, y = 130)

#info_ingresada = int(e1.get())  #revidar compatibilidad

ventana_principal.mainloop()

#%%

#FRAME

#Objetivo: Es hacer una mejor organizacion de los elementos de control

from tkinter import *

ventana_principal = Tk()

ventana_principal.geometry("800x800")

frame1 = Frame(ventana_principal)
frame1.pack()  #posicion central-superior

frame2 = Frame(ventana_principal)
frame2.pack(side = LEFT) #posicion Izquierda

frame3 = Frame(ventana_principal)
frame3.pack(side = RIGHT) #posicion detecha

boton1 = Button(frame1, text = "Aceptar", fg = "red", activebackground = "red")
boton1.pack(side = LEFT)

boton2 = Button(frame1, text = "Cancelar", fg = "brown", activebackground = "brown")
boton2.pack(side = RIGHT)

boton3 = Button(frame2, text = "Agregar", fg = "blue", activebackground = "blue")
boton3.pack(side = LEFT)

boton4 = Button(frame3, text = "Eliminar", fg = "black", activebackground = "white")
boton4.pack(side = RIGHT)

ventana_principal.mainloop()

#%%

# LABEL

from tkinter import *

ventana_principal = Tk()

ventana_principal.geometry("200x50")

var1 = StringVar()
etiqueta1 = Label(ventana_principal, textvariable = var1, relief = RAISED)

#file_dir = openfile()

var1.set("Hola buenos dias como estas?")

etiqueta1.pack()

ventana_principal.mainloop()



















