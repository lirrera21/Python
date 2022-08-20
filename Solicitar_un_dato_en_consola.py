#SOLICITAR UN NUMERO EN LA CONSOLA
edad = int(input("Ingreso su edad:"))
if edad >= 16:
    print ("Puede votar")
else:
    print ("No puede votar")

# isdecimal  se utiliza para saber si la cadena que ingresan se puede convertir en un entero

a = "Hola Mundo"
print (a.isdecimal())
a= "12"
print (a.isdecimal())

edad = ""
while type(edad) == str:
    edad = input("Ingreso su edad:")
    if edad.isdecimal():
        edad = int(edad)
    else: 
        print("Solo se permiten numeros")
if edad >= 16:
    print ("Puede votar")
else:
    print ("No puede votar")
