
numero = input("Introduce una cantidad de -> €: ") #Aquí hacemos el imput para que pregunte al usuario el siguiente texto
numero = int(numero)#Aqui transormamos la variable numero a int.
print(numero)#Aquí printamos la variable numero

iva = input("Introduce '%' de iva que quieres aplicar: ")#Aquí hacemos nuevamente el input para preguntar por consola al usuario.
iva = int(iva)#Volvemos a transformar la variable iva que por defecto será str pues la pasamos a int.
print(iva)#Aquí printamos la variable iva.

if (iva == 21):
    iva = 1.21
if (iva == 10):
    iva = 1.1
if (iva == 4):
    iva = 1.04
resultado = numero * iva
    
print ("El precio total de " + str(numero) + " aplicandole el " + str(iva)+"'%'"+ "es de: " + str(resultado))
