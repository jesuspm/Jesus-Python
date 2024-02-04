# Demanar a l’usuari posar 2 paraules.
# Afegir aquestes a una tupla i mostrar per pantalla quantes vegades apareix cada lletra.

# Pedir al usuario que introduzca dos palabras
palabra1 = input("Ingresa la primera palabra: ")  # pedimos al usuario la primera palabra
palabra2 = input("Ingresa la segunda palabra: ")  # Pedimos al usuario la segunda palabra

# Colocar las palabras en una tupla
tupla_palabras = (palabra1, palabra2)  # Aquí creamos una tupla -> tupla_palabras con las dos palabras ingresadas por el usuario

# Contar cuántas veces aparece cada letra
conteo_letras = {}  # Inicializa un diccionario para contar las letras
for palabra in tupla_palabras:  # Aquí iteramos sobre cada palabra en la tupla
    for letra in palabra:  # Aquí iteramos sobre cada letra en la palabra
        if letra.isalpha():  # Aquí comprobamos que la letra sea alfabetica
            conteo_letras[letra] = conteo_letras.get(letra, 0) + 1  # Incrementa el conteo de la letra en el diccionario

# Mostrar en pantalla el conteo de letras
print("Conteo de letras:")
for letra, cantidad in conteo_letras.items():  # Aquí iteramos sobre el diccionario de conteo de letras.
    print(f"{letra}: {cantidad} veces")  # Aquí mostramos la letra y su cantidad de apariciones.
