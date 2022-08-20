matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
# print (matriz)

fila = int(input("Ingrese la fila:"))
columna = int( input ("Ingrese la columna:"))
if (fila == 0 or fila ==1) and (columna >=0 and columna <=2):
    print (matriz[fila][columna]) 
else:
    print ("No ingreso numeros de fila y columna validos")
    while (fila == 0 or fila ==1) and (columna >=0 and columna <=2) is False :
        fila = int(input("Ingrese la fila de forma correcta:"))
        columna = int(input ("Ingrese la columna de forma correcta:"))
        if (fila == 0 or fila ==1) and (columna >=0 and columna <=2) is True:   
        print (matriz[fila][columna])
        else:
        print ("No ingreso numeros de fila y columna validos")
        

        

#else:
#print ("Fin de programa")        
            
'''if (fila == 0 or fila ==1) and (columna >=0 and columna <=2):
        print (matriz[fila][columna])
else:
        #fila = int(input("Ingrese la de forma correcta fila:"))
        #columna = int(input ("Ingrese la columna de forma correcta:")) 
    while (fila == 0 or fila ==1) and (columna >=0 and columna <=2) is False : 
                fila = int(input("Ingrese la de forma correcta fila:"))
                columna = int(input ("Ingrese la columna de forma correcta:"))   
    else:
        print (matriz[fila][columna])'''
            
        
'''while (fila != 0 or fila != 1) and (columna <=0 and columna >=2):
       fila = int(input("Ingrese la fila:"))
       columna = int( input ("Ingrese la columna:"))
                else:
                fila = int(input("Ingrese la de forma correcta fila:"))
                columna = int( input ("Ingrese la columna de forma correcta:"))
                print (matriz[fila][columna])
    break
    print ("Fin del programa")'''



# -*- coding: utf-8 -*-

''' Solucion
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
fila = int(input("Fila: "))
columna = int(input("Columna: "))
if (fila == 0 or fila == 1) and (columna >= 0 and columna <= 2):
    print(matriz[fila][columna])
else:
    print("La fila o la columna no es válida.") '''
    
