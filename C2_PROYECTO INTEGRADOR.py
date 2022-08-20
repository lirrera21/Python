#!/usr/bin/env python
# C2_Proyecto Integrador
#Crear un programa que solicite el nombre de un alumno a través de la consola, 
#y luego chequee que no esté vacío. En caso de estarlo, debe imprimir un mensaje de error;
#en caso contrario, imprimir un mensaje indicando que se ingresó correctamente.

n = input("Ingrese el nombre del alumno: ")
#print (n)
if n == "":
    print ("No es un nombre valido.")
else:  
    print ("Se ha ingresado correctamente.")
