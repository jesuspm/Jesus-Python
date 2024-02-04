import json

def leer_y_mostrar_json():
    try:
        # Leer el JSON desde el archivo externo que hemos creado anteriormente.
        with open("libros.json", "r") as file:
            json_data = json.load(file)

        # Mostrar el JSON por consola
        print("JSON leído:")
        print(json.dumps(json_data, indent=2))
    except FileNotFoundError:
        print("El archivo 'libros.json' no se encontró. Asegúrate de haber ejecutado el ejercicio anterior para crearlo.")

# Llamar a la función para leer y mostrar el JSON
leer_y_mostrar_json()
