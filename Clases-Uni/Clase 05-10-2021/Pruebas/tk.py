from tkinter import* 
def pulsar():
    valor = int(entrada.get())
    valor = valor*10
    valor = ("Numero = " + str(valor))
    etiqueta.config(text=valor)
    

ventana = Tk()
ventana.title("Mi aplicacion")
miframe = Frame(ventana)
miframe.grid(column=0,row=0,padx=(50,50),pady=(10,10))
miframe.columnconfigure(0,weight=1)
miframe.rowconfigure(0,weight=1)
#Insertanmos componentes
etiqueta = Label(miframe, text= "Numero")
etiqueta.grid(column=1, row=2, sticky=(W, E))
boton = Button(miframe, text="Pulsame", command=pulsar)
boton.grid(column=2, row=3)
numero = ""
entrada = Entry(miframe, width=15, textvariable=numero)
entrada.grid(column=2, row=2)
print(numero)


ventana.mainloop()

