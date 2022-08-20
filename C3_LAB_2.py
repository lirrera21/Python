matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
fila = int (3)
columna = int(3)
while (fila != 0 and fila != 1) and (columna != 0 or columna !=1 or columna !=2):
    fila = int(input("Ingrese la fila:"))
    columna = int( input ("Ingrese la columna:"))
    
print (matriz[fila][columna])
