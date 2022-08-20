
import tkinter as tk
#darle funcionabilidad a un boton. Primero crear una funcion, despues del import y antes de la ventana

def saludar():
    #obtener el contenido de la caja y guardarlo en una variable
    nombre = caja1.get()
    etiqueta2.config( text= "Hola " + nombre)
    
    #print ("Hola", nombre)
    #print ("Hola " +  nombre)


#crear ventana
ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title ("Mi aplicacion de tk.")
ventana.config (bg = "pink")
ventana.config(cursor="heart")

#Controles /Widgets 

#Cajas de texto
caja1 = tk.Entry()
caja1.place( x= 50, y=210,width=200, height=20)
caja1.config (bg= "white")
#etiqueta junto a la caja de texto
etiqueta1 = tk.Label(text= "Nombre:")
etiqueta1.place (x=50, y=188)
etiqueta1.config (bg="pink")

#Botones
boton1 = tk.Button(text= "Hola soy Python")
boton1.place(x=50, y=70, width=100, height=25)

boton2 = tk.Button(text= "Apreta que te saludo", command=saludar)
boton2.place(x=50, y=140, width=120, height=25)

etiqueta2 = tk.Label ()
etiqueta2.place (x=50, y= 240)

#imagen



#Pestaña

#vista de arbol

#Menu

#Barra de desplazamiento


#Mostrar la ventana (entre otras cosas).
ventana.mainloop()
