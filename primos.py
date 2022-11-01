#Algoritmo para saber si el número es primo

primo = int(input("ingrese el número que desea saber si es primo "))
esPrimo=True


if(primo<=1):
    print("no es primo")
elif(primo==2):
    print("es primo")    
else: 
    for n in range(2, primo):
        if primo % n == 0:
           esPrimo=False
           break
    if (esPrimo==True):
        print("es numero primo")
    else: 
        print("No es número primo")  
               


