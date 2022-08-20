#diferencia en usos de print y return

def aplicar_iva(precio):
    precio_con_iva = precio *1.21
    return precio_con_iva
precio = 8000
if aplicar_iva(precio) < 1500:
    print("Tenes descuento")
else:
    print("No tenes descuento")
    

#en programacion se distinguen generalemente dos componentes:
#el componente de la presentacion de los datos
#el componente de la logica de los datos
#las funciones por lo general pertenecen a la logica de los datos, revicen datos a traves de los argumentos los procesan y devuelven un resultado
#otra parte del programa, el componente de la visualizacion, va a decir que hace con esos datos si los imprime en consola, los manda a la base de datos,ect
#pero esto ultimo no tiene que estar mezclado con la logica del programa, osea no tiene que estar adentro de la funcion
#traten de evitar los print adentro de las funciones y establezacn el valor del retorno con un return

#Argumentos con nombres en funciones
#forma alternativa de indicar los valores de los argumentos al momento de llamar a una funcion


def rango(desde,hasta):
    numeros = []
    while desde < hasta:
        numeros.append(desde)
        desde += 1
    return numeros

print(rango(1,6)) #el numero 1 es desde y 6 es el hasta, porque coinciden en el orden
print (rango( hasta=6, desde=1)) #es cuando los datos no llegan en orden por decirlo de alguna forma, en esta forma ignora el orden 
