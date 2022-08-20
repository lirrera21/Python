
#from tkinter import *
#ventana=Tk()
#ventana.title("Imagen")
#ventana.geometry("400x509")
#imagen=PhotoImage("bigblue.png")
#fondo=Label(ventana,imagen=imagen).place(x=0,y=0)

#ventana.mainloop()

from tkinter import * 

ventana = Tk()

Myframe = Frame()

Myframe.pack()

Imagen=PhotoImage(file="bigblue.png")

Imagen_2 =Label(Myframe, Image=Imagen)

Imagen_2.place(x=100, y=200)

ventana.mainloop()
