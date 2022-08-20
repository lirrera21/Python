edad = int(input("Dígame su edad: "))
print(f"Su edad son {edad} años")

# la f hace que traiga edad como variable
#En versiones de Python anteriores a la versión 3.6 esto causaba problemas cuando se querían 
#incorporar variables en el argumento de la función input(), como se comenta en la lección de Temas obsoletos, 
#pero las cadenas "f" permiten hacerlo fácilmente:
# Formateo con %
# --------------

# El formato basado en % sólo es válido para los tipos de 
# datos str, int y float:

nombre = input ("Escriba su nombre: ")
edad = int(input ("Escriba su edad: "))
altura = float(input ("Escriba su altura: "))
print (nombre , edad , altura )
#print('Tiene %i años' %edad)  # Tiene 35 años
#print('%s tiene %i años y mide %f m.' %(nombre, edad, altura))
# Claudia tiene 35 años y mide 1.820000 m.

# Un objeto datetime (una hora o fecha) y otro tipo de
# objetos no pueden imprimirse sin hacer previamente una 
# conversión del tipo de dato. 

