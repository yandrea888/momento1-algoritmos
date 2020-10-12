niños = int(input("ingrese el número de niños: "))
niñas = int(input("ingrese el número de niñas: "))

porcentaje_niños = niños*100/(niños+niñas)
porcentaje_niñas = 100-porcentaje_niños

print ("Hay un" , porcentaje_niños, '%' " de niños")
print ("Hay un" , porcentaje_niñas, '%' " de niñas")