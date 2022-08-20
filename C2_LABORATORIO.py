#!/usr/bin/env python
# C2_LABORATORIO_
#Crear un programa que permita ingresar dos cadenas 
#vía la consola y luego las compare, imprimiendo un mensaje en caso que sean iguales y otro en caso que sean diferentes.

m1 = str(input ("Escribe tu mensaje: "))
m2 = str(input ("Escribe tu segundo mensaje: "))
print (m1 == m2)

if (m1 == m2):
    print ("Son iguales.")
else:
    print ("No son iguales.")
