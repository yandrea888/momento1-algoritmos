import math

n1 = int(input("ingrese el número: "))

raiz_cuadrada = math.sqrt(n1)
elevado = math.pow(n1, 2)

if n1>0 :
    print("la raiz cuadrada de {} es {}". format(n1, raiz_cuadrada))
    print("el número {} elevado a la potencia 2 es {}". format(n1, elevado))

else :
    print("Error, introduce un numero mayor que 0: ")
