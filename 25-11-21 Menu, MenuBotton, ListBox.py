# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 23:40:09 2021

@author: BrandonDLC
"""

#LISTBOX

#Opciones:

# selecmode = Numero de elementos que pueden ser seleccionados : BROWSE, SINGLE, MULTIPLE, EXTENDED

from tkinter import *

ventana_principal = Tk()
 
ventana_principal.geometry("400x400")

etiqueta1 = Label(ventana_principal, text = "Selecciona un pais de la lista siguiente:")

LB1 = Listbox(ventana_principal)

LB1.insert(1, "India")
LB1.insert(2, "USA")
LB1.insert(3, "Japon")
LB1.insert(4, "Australia")
LB1.insert(5, "Mexico")

boton1 = Button(ventana_principal, text = "Inicar Proceso", command = lambda LB1 = LB1: LB1.delete(ANCHOR))
etiqueta1.pack()
LB1.pack()
boton1.pack()

ventana_principal.mainloop()

#%%

#MENU BOTTON
    
from tkinter import *
import tkinter

ventana_principal = Tk()
 
mb = Menubutton(ventana_principal, text = "Robot", relief = RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

var1 = IntVar()
var2 = IntVar()

mb.menu.add_checkbutton(label = "Aereo", variable = var1)
mb.menu.add_checkbutton(label = "Terrestre", variable = var2)

mb.pack()

ventana_principal.mainloop()

#%%

#MENU

#Ejemplo 1: MENU SIN CASCADAS

from tkinter import *

ventana_principal = Tk()

def saludar():
    print("Hola buenos dias")
    
menubar1 = Menu(ventana_principal)
menubar1.add_command(label = "Saludar", command = saludar)
menubar1.add_command(label = "Salir", command = ventana_principal.quit)

ventana_principal.config(menu = menubar1)

ventana_principal.mainloop()

#%%

#EJEMPLO 2: MENU CON CASCADAS

from tkinter import *

def algo():
    ventana_superior = Toplevel(ventana_principal)
    boton1 = Button(ventana_superior, text = "No proceso nada")
    boton1.pack()

ventana_principal = Tk()
menubar = Menu(ventana_principal)
menu_archivo = Menu(menubar, tearoff = 0)
menu_archivo.add_command(label = "Nuevo", command = algo)
menu_archivo.add_command(label = "Abrir", command = algo)
menu_archivo.add_command(label = "Guardar", command = algo)
menu_archivo.add_command(label = "Guardar como", command = algo)
menu_archivo.add_command(label = "Cerrar", command = algo)

menu_archivo.add_separator()

menu_archivo.add_command(label = "Salir", command = ventana_principal.quit())
menubar.add_cascade(label = "Archivo", menu = menu_archivo)

menu_editar = Menu(menubar, taeroff = 0)
menu_editar.add_command(label = "Deshacer", command = algo)

menu_editar.add_separator()

menu_editar.add_command(label = "Cortar", command = algo)
menu_editar.add_command(label = "Abrir", command = algo)
menu_editar.add_command(label = "Cortar", command = algo)
menu_editar.add_command(label = "Guardar", command = algo)
menu_editar.add_command(label = "Guardar como", command = algo)
menu_editar.add_command(label = "Cerrar", command = algo)

menubar.add_cascade(label = "Editar", menu = menu_editar)

menu_ayuda = Menu(menubar, tearoff = 0)

menu_ayuda.add_command(label = "Idice", command = algo)
menu_ayuda.add_command(label = "Informacion", command = algo)
menu_ayuda.add_command(label = "Sobre...", command = algo)

menubar.add_cascade(label = "Ayuda", menu = menu_ayuda)

ventana_principal.config(menu = menubar)
ventana_principal.mainloop()










