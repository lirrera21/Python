#clase 4
#print (7 % 2) # para saber si un numero lo puedo dividir por otro y el resto me da cero, se puede dividir por ese numero sin que de un numero entero


numero = int(input("Ingresa tu numero:"))

if (numero % 2)== 0 :
    print ("el numero se puede dividir por dos")
else: 
    print ("no se puede dividir por dos")
    
# las divisiones en python siempre devuelven un numero flotante

if numero / 2 -- int:
    print ("el numero se puede dividir por dos")
else:
    print ("el numero no se puede dvidir por dos")
# por eso esta comparacion siempre va a dar falso

if type (numero / 2) -- int:
    print ("el numero se puede dividir por dos")
else:
    print ("el numero no se puede dvidir por dos")
# tambien va a dar un float porque siempre se divide da como flotante

