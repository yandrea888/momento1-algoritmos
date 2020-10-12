bachiller = input("¿Tienes el titulo de bachiller? ")

if (bachiller=="si") :
    print("Puedes acceder al grado superior")
else :
    prueba_acceso = input("¿Tienes la prueba de acceso superada?")
    if (prueba_acceso=="si") :
         print ("Puedes acceder al grado superior")
    else :
         print ("No puedes acceder a un grado superior")