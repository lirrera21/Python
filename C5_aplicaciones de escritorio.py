#aplicaciones de escritor navegan de forma nativa
#herramientas para desarrollar
#Módulos / Paquetes
#con la palabra reservada import hay algunas que estan estan instaladas 
#Libreria estandar Python39/Lib
#Modulo se llama cuando es un archivo de python 
#Paquete cuando es una carpeta
#Paquete TKINTER C:\Users\LIRRERA\AppData\Local\Programs\Python\Python38
#C:\Users\LIRRERA\AppData\Local\Programs\Python\Python38\Lib\tkinter
# no hace falta ver adentro en la documentacion de python 
#tkinter - Tk (todas esta bibliotecas para aplicaciones de escritorio estan escritas en c/c++ lenguajes muy potentes, por eso son mas complejo
#Rust nuevo lenguja que le hace competencia a c++, se utiliza para desarrollar sistemas operativos, aplicaciones de escritorio, ect..
#Tk esta escrita en c
#hay otras que sin mas complejas:
#GTK+ la que usa firefox, y el modulo para acceder se llama PyGTK
#wzWidgets - wxPython (Filezilla)
#Qt - PyQt (IOBit) son todas de uso libre salvo QT que si tu aplicacion es de codigo abierto no pagas nada, sino pagas licencia. es utilizados por empesas de anti virus ect
#pandas se usa para analisis de datos
import tkinter as tk 
# lo abreviamos porque cada vez que llamemos a una funcion hay que ponerle tk.
#la interfaz grafica tambien se programa no se crea mediante photoshop
#lo primero es crear la ventana

ventana = tk.TK() #es la funcion TK, llamamos a una funcion y guardando en esa ventana

#Mostrar la ventana

ventana.mainloop()
#esta ejecucion se va a ejecutar constantemente hasta que cierre, esta frenado en mainloop 

#Controles son todo lo que le permite al usuario tener una interfaz
#caja de texto
