edad = int(input ("Ingrese su edad:"))
print(f"Su edad son (edad) años") # ni entiendo porque aca no funciona
print(f"Su edad son {edad} años")

if edad >= 16:
    print ("Puede votar.")
else:
    print ("No puede votar.")
# sino le indico que es un numero entero va a entender que el input es un str


print("El resultado es:", edad) 
    

