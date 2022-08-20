def sumar(lista):
    resultado = 0
    for numero in lista:
        resultado = resultado + numero
    return resultado

print(sumar([1,2,3,4.5,5]))
