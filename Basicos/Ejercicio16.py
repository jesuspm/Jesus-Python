# Demanar a l’usuari una frase.
# El programa eliminarà els espais i s'afegirà a una tupla.
# Mostrar per pantalla el contingut de la tupla.

# Aquí le pedimos al usuario que ponga introduzca una frase
frase_usuario = input("Introduce una frase ")

# Aquí eliminamos los espacios y añadimos las palabras a la tupla.
tupla_palabras = tuple(frase_usuario.split())

# Aqui imprimimos la tupla.
print("Contenido de la tupla:", tupla_palabras)
