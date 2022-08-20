# Módulos / Paquetes
 
# tkinter - Tk (C/C++/Rust)
# PyGTK - GTK+ (Firefox, Geany)
# wxPython - wxWidgets (Filezilla)
# PyQt - Qt (IOBit)
 
import tkinter as tk
 
 
def saludar():
    # Obtener el contenido de la caja1 y guardarlo
    # en una variable.
    nombre = caja1.get()
    # ~ print("Hola " + nombre)
    # Cambiar el texto de la etiqueta.
    etiqueta_saludo.config(text="Hola " + nombre)
    
 
 
# Crear la ventana.
ventana = tk.Tk()
# Establecer su tamaño.
ventana.config(width=400, height=300)
# Establecer el título.
ventana.title("Mi aplicación de Tk")
 
# Crear un botón.
boton1 = tk.Button(text="Hola mundo")
# width=ancho, height=alto (todo en píxeles)
boton1.place(x=50, y=70, width=100, height=25)
 
# Crear otro botón.
boton_saludo = tk.Button(text="Saludar", command=saludar)
# Si no indico width y height, se calculan
# automáticamente.
boton_saludo.place(x=50, y=120)
 
caja1 = tk.Entry()
caja1.place(x=70, y=200, width=200, height=20)
 
etiqueta_nombre = tk.Label(text="Nombre:")
etiqueta_nombre.place(x=68, y=175)
 
etiqueta_saludo = tk.Label()
etiqueta_saludo.place(x=70, y=230)
 
# Mostrar la ventana (entre otras cosas).
ventana.mainloop()
 
RAW Paste Data
# Módulos / Paquetes

# tkinter - Tk (C/C++/Rust)
# PyGTK - GTK+ (Firefox, Geany)
# wxPython - wxWidgets (Filezilla)
# PyQt - Qt (IOBit)

import tkinter as tk


def saludar():
    # Obtener el contenido de la caja1 y guardarlo
    # en una variable.
    nombre = caja1.get()
    # ~ print("Hola " + nombre)
    # Cambiar el texto de la etiqueta.
    etiqueta_saludo.config(text="Hola " + nombre)
    


# Crear la ventana.
ventana = tk.Tk()
# Establecer su tamaño.
ventana.config(width=400, height=300)
# Establecer el título.
ventana.title("Mi aplicación de Tk")

# Crear un botón.
boton1 = tk.Button(text="Hola mundo")
# width=ancho, height=alto (todo en píxeles)
boton1.place(x=50, y=70, width=100, height=25)

# Crear otro botón.
boton_saludo = tk.Button(text="Saludar", command=saludar)
# Si no indico width y height, se calculan
# automáticamente.
boton_saludo.place(x=50, y=120)

caja1 = tk.Entry()
caja1.place(x=70, y=200, width=200, height=20)

etiqueta_nombre = tk.Label(text="Nombre:")
etiqueta_nombre.place(x=68, y=175)

etiqueta_saludo = tk.Label()
etiqueta_saludo.place(x=70, y=230)

# Mostrar la ventana (entre otras cosas).
ventana.mainloop()

Public Pastes
