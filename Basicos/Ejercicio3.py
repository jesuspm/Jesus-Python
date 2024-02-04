numero1 = input("Introduce el primer numero: ")#Aqui le pedimos al usuario que ingrese el primer numero
numero1 = int(numero1)#Aquí convertimos el numero 1 a INT

numero2 = input("introduce el segundo numero: ")#Aqui le pedimos al usuario que ingrese el segundo numero
numero2 = int(numero2)#Aquí convertimos el numero2 a INT


if(numero1>numero2):#Aquí comparamos que SI el numero1 es mas grande que el numero2 que imprima la linea 9.
    print("El numero mas grande es el --> " + str(numero1)) #Aqui lo que hacemos con el str(numero1) es convertir el numero1 a 
                                                        #STRING para que nos deje imprimirlo, ya que no se puede concatenar STRINGs + numeros
   
if(numero1<numero2):
    print("El numero mas grande es el --> " + str(numero2))#Aqui lo que hacemos con el str(numero1) es convertir el numero1 a 
                                                       #STRING para que nos deje imprimirlo, ya que no se puede concatenar STRINGs + numeros
   