# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:58:27 2021

@author: BrandonDLC
"""

from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import simplekml
import pandas

def images(b):#boton sería el parámetro recibido
   archivo = filedialog.askopenfilename(title="Documentos",initialdir="C:/",filetypes=(("Archivos .csv","*.csv"),("Archivos de Texto",
   "*.txt"),("Archivos pdf","*.pdf"),("todos los archivos","*.*")))
   if b == 1:   
      print("botón uno") #acá mostrás la imagen
      
      print(archivo)
      inicio_1=Label(ventana, text=archivo)
      inicio_1.place(x=50,y=125)
      df = pandas.read_csv(archivo)
      kml = simplekml.Kml()
      for lon, lat in zip(df["Longitude"], df["Latitude"]):
          kml.newpoint(coords = [(lon,lat)])
      
   if b == 2:
       print("Conversion lista")
       
   if b ==3:

       kml.save("D:\\Descargas\\Points.kml")
      


ventana = Tk()

ImgSub4_1 = Button(ventana, text = ("Abrir Archivo"),command = lambda:images(1)) #con lambda le pasamos un parámetro a la función
ImgSub4_1.pack()
ImgSub4_2 = Button(ventana, text = ("Convertir"),command = lambda:images(2))
ImgSub4_2.pack()
ImgSub4_3 = Button(ventana, text = ("Guardar"),command = lambda:images(3))
ImgSub4_3.pack()

ventana.mainloop()