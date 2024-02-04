#LOOPS: Mostrar els números imparells de l’1 al 500.
values = list(range(2,501,2))#El primer dos indica por que numero comenzará a imprimir, el 501 es el numero hasta el cual queremos imprimir -1, y el 2 ultimo es el salto entre
                             #un numero y otro (irá de 2 en 2).
for i in values:
    print(i)