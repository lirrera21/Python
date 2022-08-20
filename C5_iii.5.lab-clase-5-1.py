import tkinter as tk


def sumar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    etiquetar.config (a + b)


def restar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    print(a - b)
    
def dividir():
    a = int(caja_a.get())
    b = int(caja_b.get())
    print(a / b)
    
def multiplicar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    print(a * b)
   

    
ventana = tk.Tk()
ventana.config(width=200, height=200)
ventana.title("Calculadora")

etiquetaa = tk.Label(text= "A:")
etiquetaa.place (x=5, y=20)
etiquetaa.config (bg="pink")

caja_a = tk.Entry()
caja_a.place(x=30, y=20, width=50, height=25)

etiquetab = tk.Label(text= "B:")
etiquetab.place (x=5, y=60)
etiquetab.config (bg="pink")

caja_b = tk.Entry()
caja_b.place(x=30, y=60, width=50, height=25)

boton = tk.Button(text="+", command=sumar)
boton.place(x=20, y=100, width=20, height=20)
boton.config (bg="pink")

boton = tk.Button(text="-", command=restar)
boton.place(x=60, y=100, width=20, height=20)
boton.config (bg="pink")

boton = tk.Button(text="/", command=dividir)
boton.place(x=100, y=100, width=20, height=20)
boton.config (bg="pink")

boton = tk.Button(text="*", command=multiplicar)
boton.place(x=140, y=100, width=20, height=20)
boton.config (bg="pink")

etiquetac = tk.Label(text= "Resultado:")
etiquetac.place (x=20, y=150)

etiquetar = tk.Label()
etiquetar.place (x=80, y=150)
etiquetar.config (bg="pink")

ventana.mainloop()
