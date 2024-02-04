# El mateix que l’anterior exercici, però sense demanar un màxim de números.
# L’usuari indicarà quan ha acabat posant un 0.


# Inicializamos una lista para almacenar los números introducidos y mas adelante la convertiremos en tupla.
numeros = []

# Pedir al usuario que introduzca números hasta que se ingrese el numero 0
while True:
    entrada = input("Introduce un número (o 0 para terminar): ")
    
    # Comprobamos si el usuario ha introducido 0 para salir del bucle
    if entrada == '0':
        break
    
    # Aquí intentamos convertir la entrada de la lista en un numero, y si no es un numero valido salta al except
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, introduce un número válido.")

# Aquí ordenamos la lista de números y la convertimos en una tupla
tupla_numeros = tuple(sorted(numeros))

# Muestra por pantalla el contenido de la tupla
print("Tupla ordenada:", tupla_numeros)
