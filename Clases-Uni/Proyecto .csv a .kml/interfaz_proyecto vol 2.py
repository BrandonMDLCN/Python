# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:27:38 2021

@author: julio medina
"""
#libererias leidas
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import simplekml
import pandas

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

image=Image.open("D:\\Descargas\\tierra1.jpeg")
image=image.resize((50,50),Image.ANTIALIAS)

img=ImageTk.PhotoImage(image)
lbl_img=Label(ventana_principal,image=img)
lbl_img.place(x=0,y=0)

#Metodos

def abrir_archivo():
    global archivo
    archivo = filedialog.askopenfilename(title="Documentos",initialdir="C:/",filetypes=(("Archivos .csv","*.csv"),("todos los archivos","*.*")))
    print(archivo)
    inicio_1=Label(ventana_principal, text=archivo)
    inicio_1.place(x=50,y=120)
    
def convertir_archivo():
    global kml
    kml = simplekml.Kml()
    df = pandas.read_csv(archivo)
    for lon, lat in zip(df["Longitude"], df["Latitude"]):
          kml.newpoint(coords = [(lon,lat)])
    inicio_2=Label(ventana_principal,text="Conversión Lista")
    inicio_2.place(x=50,y=220)
    

def guardar():
    global archivo_guardar
    archivo_guardar = filedialog.askdirectory()
    global result
    result=text.get()
    print(result)
    nuevo_nombre=archivo_guardar+"/"+result+".kml"
    print(nuevo_nombre)
    kml.save(nuevo_nombre)

#
boton_archivo = Button(ventana_principal,text="buscar archivo",command=abrir_archivo,width=11,height=3)
boton_archivo.place(x=300,y=100)

boton_convertir = Button(ventana_principal,text="convertir archivo",command=convertir_archivo,width=12,height=3)
boton_convertir.place(x=300,y=200)
boton_guardar=Button(ventana_principal, height=1, width=10, text="Guardar", command=guardar)
boton_guardar.place(x=200,y=350)

nombre = Label(ventana_principal, text = "Ingresa nombre del archivo a crear").place(x = 30, y = 300)

text=Entry(ventana_principal)
text.place(x = 250, y = 300)

ventana_principal.mainloop()
