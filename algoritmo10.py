num = int(input("Ingrese un número: "))

while num==0 :
    print("El número", num, "no es par ni impar")
    num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print('El número', num, 'es par.')    
else :
    print('El número', num, 'es impar.')

 