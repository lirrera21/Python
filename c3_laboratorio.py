fila = ""
while type (fila) == str:
    fila = input("Ingresa nombre fila:")
    if fila.isdecimal():
        fila = int(fila)
    else:
        print("Por favor ingresa un numero")