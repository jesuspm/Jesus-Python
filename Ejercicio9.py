#Demanar a l’usuari que posi dues paraules. Al executar el programa, mostrarà per pantalla 
#les dues paraules amb els dos primers caràcters de cada paraula intercanviats. 
#Exemple: Quatre Camins passaria a 
#         Caatre Qumins.

palabra1 = input("Introduce la PRIMERA palabra: ")
palabra2 = input("Introduce la SEGUNDA palabra: ")

#Aquí lo que hago es que cojo las primeras 2 letras de palabra2 -> [0:2] y de la palabra1 de la posicion 2 hasta el final de la palabra ->  [2:]
print(palabra2[0:2]+palabra1[2:])
print(palabra1[0:2]+palabra2[2:])

