#buscar un numero primo
#numeros primos; 2,3,5,7,11,13,17

numero = int(input("Ingrese numero:"))

primo = True

for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False
        break
if primo:
    print ("El numero es primo")
else:
    print ("El numero no es primo")


# Crear un programa que solicite un número entero 
# por la consola e indique si es primo o no.
# Números primos: 2, 3, 5, 7, 11, 13, 17
 
numero = int(input("Ingrese un número: "))
primo = True
 
for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False
        break
 
if primo:
    print("El número es primo.")
else:
    print("El número no es primo.")
