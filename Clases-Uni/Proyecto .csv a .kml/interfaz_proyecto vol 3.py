# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:37:31 2021

@author: BrandonDLC
"""

#libererias leidas
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import simplekml
import pandas
from tkinter import messagebox
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

def abrir_archivo():
    global archivo
    archivo = filedialog.askopenfilename(title="Documentos", initialdir="C:/", filetypes=[("Archivos .csv", "*.csv")])
    print(archivo)
    global inicio_1
    inicio_1=Label(ventana_principal, text=archivo)
    inicio_1.place(x=50,y=120)
  
def convertir_archivo():
    try:
        global kml
        kml = simplekml.Kml()
        df = pandas.read_csv(archivo)
        for lon, lat in zip(df["Longitude"], df["Latitude"]):
              kml.newpoint(coords = [(lon,lat)])
        global inicio_2
        inicio_2=Label(ventana_principal,text="Conversión Lista")
        inicio_2.place(x=50,y=220)
        
    except UnicodeDecodeError:
        messagebox.showwarning(message='Debes cargar un archivo .csv', title="Error")
    except NameError:
        messagebox.showwarning(message='Primero se debe cargar un archivo', title="Error")
        del kml

def guardar():
    try:
        global archivo_guardar
        archivo_guardar = filedialog.askdirectory()
        global nn
        nn = text.get()
        print(nn)
        nuevo_nombre = archivo_guardar + "/" + nn + ".kml"
        print(nuevo_nombre)
        kml.save(nuevo_nombre)
        messagebox.showinfo(message='Archivo Guardado', title="Listo")
        inicio_1.destroy()
        inicio_2.destroy()
        text.delete(0, END)
        del archivo_guardar
        %reset -f
        
    except OSError:
        messagebox.showwarning(message='Los nombres del archivo no pueden tener contener ninguno de los siguientes caracteres: /:*"?\<>|', title="Error")
    except NameError:
        messagebox.showwarning(message='Primero se debe cargar un archivo', title="Error")

#Lo que  hay en la ventana Principal
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
