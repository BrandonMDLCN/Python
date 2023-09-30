# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:07:33 2021

@author: BrandonDLC
"""

# Opciones:
    
# id = C.create_art(x0, y0, y1, option, ...) = Crea arcos o circulos
# id = C.create_bitmap(x, y, options ...) = Crea mapas de bit
# id = C.create_image(x, y, option, ...) = Carga una imagen en el canvas
# id = C.create_line(x0, y0, x1, y1, ..., xn, yn, option, ...) = Crea lineas
# id = C.create_oval(x0, y0, x1, y1, option, ...) Crea elipses
# id = C.create_polygon(x0, y0, x1, y1, option, ...) = Crea poligonos
# id = C.create_rectangle(x0, y0, x1, y1, option, ...) = Crea rectangulos
# id = C.create_text(x, y, option, ...) = Muestra un texto en el canvas
# id = C.create_window(x, y, option, ...) = Coloca un elemento de control en el canvas

# pueden cambiar "id" y "C" : le pueden poner el nombre que sea

import tkinter

ventana_principal = tkinter.Tk()

canvas1 = tkinter.Canvas(ventana_principal, bg = "blue", height = 250, width = 300)

coord = 10, 50, 240, 210

#Creamos un arco
arc = canvas1.create_arc(coord, extent = 180, fill = "red")

canvas1.pack()

ventana_principal.mainloop()

#%%

# CHECKBUTTON

# Opciones:

# onvalue = Estado del boton al hacer click
# offvalue = Estado del boton al no hacer click
# varaible = variable necesaria para rastrear el estado del boton
# command = Llamar la funcion que representa la accion del boton

from tkinter import *

ventana_principal = tkinter.Tk()

CheckVar1 = IntVar() #IntVar(), FloatVar(), StringVar()
CheckVar2 = IntVar()

CB_1 = Checkbutton(ventana_principal, text = "Musica", variable = CheckVar1, onvalue = 1, offvalue = 0, height = 5, width = 20)
CB_2 = Checkbutton(ventana_principal, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height = 5, width = 20)

CB_1.pack()
CB_2.pack()

ventana_principal.mainloop()












