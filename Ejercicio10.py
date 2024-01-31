import random
#Crear un arxiu on caldrà endevinar el número escollit pel programa entre 1 i 100.
#Cada vegada que l’usuari hi posi un número,caldrà indicar si és més petit o més gran fins que encerti i el missatge haurà d’indicar que ha encertat. 
#Indicar també el número d’intents.

#Aquí asignamos a la variable numeroSecreto la funcion random.randint(1,100) para que de forma aleatoria el sistema printee un numero del 1 al 100
numeroSecreto = random.randint(1, 100)
#Aquí únicamente printeamos un string con el numero secreto.
resultado = print("El numero secreto es --> " +str(numeroSecreto))
#Inicializamos contador.
intentos = 5
#Aqui metemos el input para el usuario
pregunta = input("Adivina el numero secreto, esta entre el 1 y el 100: ")
#convertimos la variable pregunta(String) a int en la siguiente linea.
pregunta = int(pregunta)

#Aquí decimos que mientras 'pregunta' sea DIFERENTE a numeroSecreto irá filtrando con las siguientes condiciones.
while pregunta != numeroSecreto:
    #Si el numero que introduce el usuario es MAYOR al numero
    if pregunta>numeroSecreto:
        print("Error el numero secreto es más pequeño!")
        intentos+= -1
        print("Numero de intentos" +str(intentos))

    if pregunta<numeroSecreto:
        print("Error, el numero es más grande")
        intentos+= -1
        print("Numero de intentos " +str(intentos))
    
    if intentos == 0:
        print("Se te han terminado los intentos!")
        break
    pregunta = int(input("Escribe un numero del 1 al 100: "))
    
if pregunta == numeroSecreto:
        print("Has acertado!")
