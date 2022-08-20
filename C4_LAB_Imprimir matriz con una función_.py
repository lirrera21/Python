m1 = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
#print (m1)

def imprimir_m1 (fila, columna):
    for x in m1: 
        print([fila],[columna])

imprimir_m1 (0,1)


def imprimir_matriz(matriz):
    for fila in matriz:
        for numero in fila:
            print(numero)

m1 = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
m2 = [[4.3, 7.1, 4.0], [5.9, 6.7, 7.4]]
m3 = [[5.3, 8.1, 4.0], [6.9, 7.7, 8.4]]
imprimir_matriz(m1)
imprimir_matriz(m2)
imprimir_matriz(m3)
