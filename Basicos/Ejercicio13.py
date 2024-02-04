# Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula de multiplicar fins el 10. 
# Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30

#Le pedimos al usuario que introduzca un numero del 1 al 10
entrada = int(input("introduce un numero del 1 al 10: ")) 

#Aquí es donde aplicamos una condicion: Si el numero es menor o igual a lo que le pasa el usuario por entrada entrará dentro.
if 1<= entrada <=10:
    
    #Aquí creamos la lista la cual ira multiplicando mas adelante nuestra entrada.
    numeroXmultiplicar = [1,2,3,4,5,6,7,8,9,10]
    
    for i in numeroXmultiplicar:
        operacion = int(entrada*i)
        operacion = int(operacion)
        print(operacion)
        
else:
    print("Error, el numero introducido no es valido.")