#clase 4
#Definir una funcion
def imprimir_saludo():
    print ("Hola Mundo")
    

#Crear variables
a= 7
b = 5
print ( a+ b) 

#Ejecutar o llamar a una funcion previamente definida

imprimir_saludo()

#defino funcion con argumento
def imprimir_saludos (destinatario):
    print ("Hola " + destinatario )
    print ("Chau " + destinatario )

#llamo funcion con variables de esos argumentos

imprimir_saludos("Juan")
imprimir_saludos("Zuma")

#print (destinatario) # no es valido porque la variable destinatario tiene visibilidad dentro de las funciones


#defino funcion con mas de un argumento

def imprimir_salu2 (destinatario, lenguaje, cantidad):
    print ("Hola ", destinatario, "se que usas el leguaje", lenguaje, "porque lo usaste ", cantidad, " de veces")

imprimir_salu2 ("Juan","Python","2")

imprimir_salu2 ("Toto","Java","mil veces")


def aplicar_iva (precio):
    precio_con_iva = precio * 1.21
    return precio_con_iva

resultado = aplicar_iva(1000)
print (resultado)
print (aplicar_iva(1000))

#dentro de una funcion puedo tener un resultado y tambien todas las estructuras

def aplicar_iva (precio):
    if precio > 1000:
        precio_con_iva = precio 
    else:
        precio_con_iva = precio * 1.21
    return precio_con_iva

resultado = aplicar_iva(1000)
print (resultado)
print (aplicar_iva(800))

#de una funcion puedo devolver multiples valores, pero solo permite un return establece un resultado y finaliza la funcion

def min_y_max(lista):
    a= min (lista)
    b= max (lista)
    return [ a, b ] # ese unico valor que me permite retornar puede ser una lista y asi traer mas de un resultado
    
print (min_y_max([4,7,9,1,13]))
