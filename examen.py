a=1
b=7

resultado = (a >= 2 and b < 8) == (not a >1 or a ==2) and b< 7
print (resultado)

resultado = (a >= 2 and b < 8) == (b<=7) and (a==2 or a>=2)
print (resultado)
