#Programa que pedirá dos numeros y los multiplicaremos y sumaremos y dividiremos.

numero1 = input("Introduce el primer numero: ")
numero1 = int(numero1)

numero2 = input("introduce el segundo numero: ")
numero2 = int(numero2)

#MULTIPLICACION
multiplicar = numero1 * numero2
print(str(numero1) + "x" +str(numero2) + ":" +str(multiplicar))

#SUMA
suma = numero1 + numero2
print(str(numero1) + "+" + str(numero2) + ":" + str(suma))

#DIVISION
division = numero1 / numero2
print(str(numero1) + "/" + str(numero2) + ":" + str(division))