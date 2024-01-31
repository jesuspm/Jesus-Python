import random
#Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100.
#Cada vegada que l’usuari hi posi un número,caldrà indicar si és més petit o més gran fins que encerti i el missatge haurà d’indicar que ha encertat. 
#Indicar també el número d’intents.

numeroSecreto = random.randint(1, 100)#random

resultado = print("El numero secreto es --> " +str(numeroSecreto))


intentos = 5

pregunta = input("Adivina el numero secreto, esta entre el 1 y el 100: ")
pregunta = int(pregunta)

while pregunta != numeroSecreto:
    
    if pregunta>numeroSecreto:
        print("Error el numero secreto es más pequeño!")
        intentos-1
        
        
    if pregunta<numeroSecreto:
        print("Error, el numero es más grande")
        intentos-1
        
        #print("Numero de intentos" +str(intentos))
        
    if intentos ==0:
        break
    pregunta = input("Escribe un numero del 1 al 100: ")
    
if pregunta == numeroSecreto:
        print("Has acertado!")
