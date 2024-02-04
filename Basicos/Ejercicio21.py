# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista. Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.

# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:

# Aquí pedimos al usuario que ingrese 10 números separados por espacios
entrada_usuario = input("Introduce 10 números separados por espacios: ")

# Convertimos la entrada del usuario en una lista de números
numeros = [float(x) for x in entrada_usuario.split()]

# Calcular la suma y la media
suma_total = sum(numeros)
media = suma_total / len(numeros)

# Aquí agregamos la suma y la media a la lista
numeros.append(suma_total)
numeros.append(media)

# Mostrar por pantalla la lista y los resultados
print("Números del usuario:")
print(numeros)
print("Suma total:", suma_total)
print("Media:", media)

