#creamos un diccionario vacio
alumos = {}

#ejecutar este codigo infinitamente
while true:
    print ("Ingrese el numero de la operacion que desea ejecutar:")
    print ("1- Ver lista de alumnos")
    print ("2 - Añadir alumno a la lista.")
    print ("3- Ver cantidad de cursos de un alumno.")
    print ("4- Salir.")
    opcion = input()

    if opcion == "1":
        print ("Lista de alumnos:")
# el bucle for aplicado sobre un diccionario recorre sus claves
        for nombres in alumnos:
            cursos = alumnos[nombre]
        #necesito convertir cursos a una cadena para poder concatenarlo
        print (nombre + " - " + str(cursos) + "cursos")
    elif opcion == "2":
        nombre_alumno = input ("Ingrese el nombre del alumno:")
# es condicion que la cantidad de cursos sea un numero entero, necesitamos convertirlo
#ya que el resultado de input() siempre sera una cadena
        cursos = int(input("Ingrese cantidad de cursos:")
        if nombre_alumno == "" :
            print ("Error: no ha ingresado un valido.")
        else:
            alumnos[nombre_alumno] = cursos
            print ("Haz ingresado el alumno correctamente.")
      
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno:")
        print("Cursos" + str(alumnos[nombre]))
    elif == "4":
    #forzar el bucle a que termine
    break
else: 
    print ("La opcion ingresada no es correcta, intentalo de nuevo.")
print ("¡Gracias por utilizar nuestro programa!")

