#!/usr/bin/env python
# -*- coding: utf-8 -*-

matriz = []
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

for numero_fila in range(0, filas):
    matriz.append([])
    for numero_columna in range(0, columnas):
        numero = int(input("Ingrese el número para matriz[" + str(numero_fila) + "][" + str(numero_columna) + "]: "))
        matriz[numero_fila].append(numero)

print("La matriz ingresada es:")
print(matriz)
