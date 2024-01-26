#Demanar a l’usuari un número. Indicar si el número inserit per l’usuari és parell o senar.
numero1 = input("introduce un numero para comprobar: ")
numero1 = int(numero1)

if(numero1 %2):
    print("Es impar")
else:
    print("Es par")
