#!/usr/bin/env python
#resolver el polinomio de 2do grado
#1) b  ** 2
#2) 4 *a*c
#3) p1 -p2
#4) raiz del paso 3
#5) -b + paso4
#6) 2 x a
#7) paso 5 /paso 6

#print ("Ingrese los valores:")
#a = input (" a= ")
#b = input (" b= ")
#c = input (" c= ")
#p1 - #p2 
#delta = (b**2) - (4*a*c)

#Polinomia se 2do grado
#a = 1
#b = 1
#c = -6
print ("Ingrese los valores:")
a = int (input (" a= "))
b = int( input (" b= "))
c = int( input (" c= "))
#Paso 1
print ("Paso 1:")
paso_1 = b**2 # o b*b
print (paso_1) 
#Paso 2
print ("Paso 2:")
paso_2 = 4*a*c
print (paso_2)
#Paso 3
print ("Paso 3:")
paso_3 = paso_1 - paso_2
print (paso_3)
#Paso 4
print ("Paso 4:")
paso_4 = paso_3 ** 0.5
print (paso_4)
#Paso 5
print ("Paso 5:")
paso_5 = -b + paso_4
print (paso_5)
#Paso_6
print ("Paso 6:")
paso_6 = 2 *a
print (paso_6)
#Paso 7
print ("Resultado1:")
paso_7 = paso_5 / paso_6
print (paso_7)
#Paso 8
print ("Resultado2:")
paso_8 = -b - paso_4
#Paso 9
paso_9 = paso_8/ paso_6
print (paso_9)


##x = -b + ((b ** 2 - 4 *a*c )** 0.5) / 2*a
##print (x)
##-x = -b - ((b ** 2 - 4 *a*c) ** 0.5 )/ 2*a
##print (-x)





