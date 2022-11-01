#
#Programa para encontrar el tesoro 
#

print("¡¡¡¡encuentra el tesoro tienes que elegir entre opciones!!! ")

reinicio = 0

while reinicio < 1 :

    opcion=int(input("Estas en un barco, ¿deseas bajar? si=1 no =0 " ))
    if(opcion == 0):
        print("fin del juego tienes que salir del barco porque te estrellas y mueres")
    elif(opcion == 1):
        print("has llegado a la isla del crustaceo ")
        print("selecciona que herramienta deseas: \n1.espada \n2.pala \n3.arco \n4.fusil ")
        opcion=int(input("escoge una herramienta "))
        if(opcion==1):
             print("escogiste espada dificulta media")
        elif(opcion==2):
            print("escogiste la dificultad dificil con pala te demoras más en derrotar a tus enemigos")
        elif(opcion==3):
             print("escogiste arco dificultad media")
        elif(opcion==4):
             print("escogiste el fusil dificultad facil")   
        opcion=int(input("escoge el camino por el que ir: 1.Cueva  2.Bosque ")) 
        if(opcion== 1):  
            print("fuiste comido por los osos de la cueva GAME OVER!!") 
        elif(opcion== 2):
            print("sigue avanzando")
            opcion=int(input("hay dos maneras de llegar a un tesoro \
                1.coger las piolets, pasar por el puente de madera sin tocar la arena movediza   \
                2. coger el traje de antiserpientes, enfrentarse a ellas y correr hacía la salida del monte"))
            if(opcion == 1):
                print("!!!FELICIDADES, ENCONTRASTE ORO¡¡¡")
            elif(opcion == 2):
                print("!!!FELICIDADES, HAS ENCONTRADO RELIQUIAS ANTIGUAS¡¡¡")    
        else:
            print("Error del juego")

    else:
        print("error opción no valida")    

    reinicio = input("¿deseas seguir en el programa? si= 0 no = 1  \n")
    reinicio = int(reinicio) 
  