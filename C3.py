# int, str, float, bool
#Listas =list
#Las listas son coleccion ordenadas de objetos

alumnos = [ "Juan", "Matias", "Sofia" ]

#ESTA LISTA DE ALUMNOS TIENE 3 ELEMENTOS CON indice desde cero 0-1-2
print (alumnos [0])
print (alumnos [1])
print (alumnos [2])

#instruccion apend el nombre de la lista . append (el elementos que queremos agregar)
#instruccion insert lista.insert(aca indicamos el indice donde lo quiero agregar 2, "Josefina")
#cambiar el nombre alumnos[3] ="Mateo" cambia uno por el otro
#eliminar un elemento del alumnos [el indice del elemento]

alumnos = [ ["Juan",2] , ["Matias",5], ["Sofia",3]]

print (alumnos[0][1]) #Si quiero la cantidad de cursos
print (alumnos[0][0]) #Si quiero acceder al nombre Juan

#se pueden simular matrices _ listas adentro de otras listas_
m = [[1,2,3],[4,5,6],[7,8,9]] #o para que se vea mas claro que es una matriz
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print (m [0][1])
print (m [2][2])
m [2][2] = 15
print (m [2][2])

