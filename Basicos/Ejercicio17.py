# Aquí pedimos al usuario que introduzca una frase.
frase_usuario = input("Introduce una frase: ")

# Eliminamos los espacios y añadimos las palabras a la tupla a tupla_palabras.
tupla_palabras = tuple(frase_usuario.split())

# Aquí eliminamos los caracteres repeditos y añadimos la frase a una tupla.
# Gracias al key=frase_usuario.index los caracteres se ordenan según su posición original de la frase introducida por el usuario.
frase_sin_repetidos = ''.join(sorted(set(frase_usuario), key=frase_usuario.index))
tupla_frase_sin_repetidos = (frase_sin_repetidos)

# Aquí mostramos el contenido.
print("Contenido de la tupla_palabras", tupla_palabras)
print("Contenido de la tupla de frase_sin_repetidos:", tupla_frase_sin_repetidos)
