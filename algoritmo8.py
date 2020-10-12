importe = int(input("ingrese el valor de la compra: "))
mes = input("ingrese el mes: ")

totalDes = importe*0.85

if (mes == "octubre") :
    print("El valor del importe con descuento es de: $", totalDes)
else :
    print("El valor del importe con descuento es de: $" , importe)
