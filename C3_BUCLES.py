## BUCLE WHY EL FLUJO DEL CODIGO PUEDE CAMBIAR, Y UN BLOQUE DE CODIGO PUEDE EJECUTARSE MAS DE UNA VEZ SIN TENER QUE REPETIRLA LITERALMENTE
# BUCLE FOR PARA
#BUCLE WHILE MIENTRAS

alumnos = ["Juan","Sofia","Pablo"]

for x in alumnos:
    print ("Hola mundo", x)
    
print ("Fin del bucle")

## x es una variable y el valor que tiene lo asigna python,y es cada uno de los valores de la lista

for x in alumnos:
    print ("Hola mundo")
    print (alumnos)
print ("Fin de bucle")


# for el criterio es la cantidad de elementos dentro de una lista, por eso requiere lista
# while necesita un condicional
# la varibale deberia cambiar para que en algun momento termine

a = 1
while a < 5 :
    print ("Hola Mundo")
    a = a + 1
print ("Fin del programa")

#range
numeros = [1,2,3,4,5] # del 1 al 20 porque es el ultimo nuemto menos 1
for numero in numeros:
    print(numero)

numeros = range(1,7) # del 1 al 20 porque es el ultimo nuemto menos 1
for numero in numeros:
    print(numero)

#o 
for numero in range (1,8):
    print (numero)

#si quiero imprimir una cantidad veces algo pero no tengo una lista

for x in range(5):
    print("Hola Mundo")

# o tambien utilizamos los valores de range sin poner la x

for _ in range (2):
    print ("Hola munde")

#Break y continue que pueden ser utilizadas adentro de un bucle for o while
#continue
#break
#continue: seguir con el siguiente elemento
primos = (1,2,3,5,7,11,13)
for numero in primos:
    if numero == 5: # o != cuando es distinto
        continue
    print (numero)

for numero in primos:
   if numero != 5:
    print (numero)
    
#break rompe el bucle, que termine aunque faltan condiciones o lista por recorrer
# break es abortar el bucle
for numero in primos:
    if numero == 5: # o != cuando es distinto
        break
    print (numero)
print("Fin del programa")

#conversion de tipo de dato
celular = "1155"
celular1 = int(celular) +1
print (celular)
print (celular1)
celular2 = str (celular)
)
#no son tan frecuentes pero se puede realizar conversion de numero flotante o boleanos
