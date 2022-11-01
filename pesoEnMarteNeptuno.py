"""crea un codigo en python que te permita
ingresar tu peso en la tierra y este lo
convierta a tu peso en marte y neptuno
Pueden hacerlo grupal o indiviudal ustedes
escogen"""

tierra = input("ingresa tu peso en kg: ")

peso_tierra= float(tierra)


    
peso_marte = (peso_tierra/9.81)*3.711
peso_neptuno = (peso_tierra/9.81)*11

print("el peso que tendrías en marte es: ", peso_marte)
print("el peso que tendrías en neptuno es ", peso_neptuno)

