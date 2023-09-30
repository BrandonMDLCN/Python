# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:27:38 2021

@author: julio medina
"""
#libererias leidas
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

#creacion de la interfaz

ventana_principal = Tk()
ventana_principal.title("convertidor de CSV a KML")
ventana_principal.geometry("500x500")
ventana_principal.resizable(width=False, height=False)
ventana_principal.config(bg="grey")
inicio=Label(ventana_principal, text="convertidor de Archivo CSV a Archivo KML",font=("Arial",13))
nombre=Label(ventana_principal,text="Earthcode")
nombre.place(x=0,y=50)
inicio.place(x=100,y=10)

def abrir_archivo():
    archivo = filedialog.askopenfilename(title="Documentos",initialdir="C:/",filetypes=(("Archivos de Texto",
    "*.txt"),("Archivos pdf","*.pdf"),("todos los archivos","*.*")))
    print(archivo)
    inicio_1=Label(ventana_principal, text=archivo)
    inicio_1.place(x=50,y=125)
    
boton_archivo = Button(ventana_principal,text="buscar archivo",command=abrir_archivo,width=11,height=3)
boton_archivo.place(x=300,y=100)

boton_convertir = Button(ventana_principal,text="convertir archivo",width=12,height=3)
boton_convertir.place(x=300,y=200)
boton_guardar=Button(ventana_principal,text="guardar archivo",width=11,height=3)
boton_guardar.place(x=200,y=350)


ventana_principal.mainloop()
