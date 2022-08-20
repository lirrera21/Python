import tkinter as tk
 
 
def puede_votar():
    edad = caja_edad.get()
    if edad.isdecimal():
        edad = int(edad)
        if edad >= 16:
            mensaje = "Puede votar."
        else:
            mensaje = "No puede votar."
        etiqueta_resultado.config(text=mensaje)
    else:
        etiqueta_resultado.config(text="Ingrese un número.")
 
range
for
in
while

if 
else
def

 
ventana = tk.Tk()
ventana.title("¿Puede votar?")
ventana.config(width=300, height=200)
 
etiqueta_edad = tk.Label(text="Edad:")
etiqueta_edad.place(x=10, y=10)
 
caja_edad = tk.Entry()
caja_edad.place(x=50, y=10, width=50, height=20)
 
boton_calcular = tk.Button(text="Calcular", command=puede_votar)
boton_calcular.place(x=110, y=8, width=60, height=25)
 
etiqueta_resultado = tk.Label()
etiqueta_resultado.place(x=10, y=90)
 
ventana.mainloop()
