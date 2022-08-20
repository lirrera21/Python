edad = ""
while type (edad) == str:
    edad = input("Ingresa tu edad:")
    if edad.isdecimal():
        edad = int(edad)
    else:
        print("Solo se permiten numeros")
    
if edad >= 16:
    print ("Poder votar.")
else:
    print ("No podes votar.")
