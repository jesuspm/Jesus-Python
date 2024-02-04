# Inicializar el diccionario de contactos
diccionario_contactos = {}

# Aquñi hacemos un bucle para ingresar contactos
while True:
    nombre = input("Ingresa el nombre del contacto (o 'fin' para terminar): ")
    
    # Verificar si el usuario quiere salir del bucle
    if nombre.lower() == 'fin':
        break
    
    # Verificar si el nombre ya está en el diccionario
    if nombre in diccionario_contactos:
        print(f"El nombre '{nombre}' ya está en el diccionario. No se añadirá de nuevo.")
    else:
        # Si el nombre no está en el diccionario, solicitar la edad y agregar al diccionario
        try:
            edad = int(input("Ingresa la edad del contacto: "))
            diccionario_contactos[nombre] = edad
        except ValueError:
            print("Por favor, ingresa una edad válida.")

# Mostrar el diccionario de contactos
print("Diccionario de contactos:")
for nombre, edad in diccionario_contactos.items():
    print(f"{nombre}: {edad} años")
