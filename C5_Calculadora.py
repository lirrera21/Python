import tkinter as tk




def sumar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    sumar = a + b
    return var.set(sumar)
    

def restar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    restar = a - b
    return var.set(restar)
    
def dividir():
    a = int(caja_a.get())
    b = int(caja_b.get())
    dividir = a / b
    return var.set(dividir)
    
def multiplicar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    multiplicar = a * b
    return var.set(multiplicar)
   

    
ventana = tk.Tk()
ventana.config(width=200, height=200)
ventana.title("Calculadora")
var = tk.StringVar()

etiqueta_a = tk.Label(text= "A:")
etiqueta_a.place (x=5, y=20)
etiqueta_a.config (bg="pink")

caja_a = tk.Entry()
caja_a.place(x=30, y=20, width=50, height=25)

etiqueta_b = tk.Label(text= "B:")
etiqueta_b.place (x=5, y=60)
etiqueta_b.config (bg="pink")

caja_b = tk.Entry()
caja_b.place(x=30, y=60, width=50, height=25)

boton_s = tk.Button(text="+", command=sumar)
boton_s.place(x=20, y=100, width=20, height=20)
boton_s.config (bg="pink")

boton_r = tk.Button(text="-", command=restar)
boton_r.place(x=60, y=100, width=20, height=20)
boton_r.config (bg="pink")

boton_d = tk.Button(text="/", command=dividir)
boton_d.place(x=100, y=100, width=20, height=20)
boton_d.config (bg="pink")

boton_m = tk.Button(text="*", command=multiplicar)
boton_m.place(x=140, y=100, width=20, height=20)
boton_m.config (bg="pink")

etiqueta_c = tk.Label(text= "Resultado:")
etiqueta_c.place (x=20, y=150)

etiqueta_r = tk.Label(textvariable=var)
etiqueta_r.place (x=80, y=150)
etiqueta_r.config (bg="pink")

ventana.mainloop()
