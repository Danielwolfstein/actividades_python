"""crea un codigo en python que te permita
ingresar tu peso en la tierra y este lo
convierta a tu peso en marte y neptuno
Pueden hacerlo grupal o indiviudal ustedes
escogen"""

reinicio = 0

while reinicio < 1 :
    tierra = input("ingresa tu peso en kg: ")
    peso_tierra= float(tierra)
    print("¿qué planeta del sistema solar  deseas hallar el peso?")
    planeta = input("1. mercurio  \n2.venus \n3.marte \n4.jupiter \n5.saturno \n6.urano \n7.neptuno \n8.pluton\n")
    planeta = int(planeta)
    if (planeta == 1):
        peso_mercurio=(peso_tierra/9.81)*3.70
        print("el peso que tendrías en mercurio es ", peso_mercurio)
    elif (planeta == 2):
        peso_venus=(peso_tierra/9.81)*8.87 
        print("el peso que tendrías en neptuno es ", peso_venus) 
    elif (planeta == 3):
        peso_marte = (peso_tierra/9.81)*3.711 
        print("el peso que tendrías en marte es ", peso_marte) 
    elif (planeta == 4):
            peso_jupiter=(peso_tierra/9.81)*23.12 
            print("el peso que tendrías en jupiter es ", peso_jupiter) 
    elif (planeta == 5):
        peso_saturno=(peso_tierra/9.81)*8.96
        print("el peso que tendrías en saturno es ", peso_saturno) 
    elif (planeta == 6):
        peso_urano=(peso_tierra/9.81)*8.69
        print("el peso que tendrías en urano es ", peso_urano) 
    elif (planeta == 7):
        peso_neptuno = (peso_tierra/9.81)*11
        print("el peso que tendrías en neptuno es ", peso_neptuno) 
    elif(planeta == 8):
        peso_pluton = (peso_tierra/9.81)*0.81
        print("el peso que tendrías en plutón es ", peso_pluton) 
    else:
        print("error número invalido")    

    reinicio = input("¿deseas seguir en el programa? si= 0 no = 1  \n")
    reinicio = int(reinicio) 
    if( reinicio == 1):
        reinicio +=1
    






