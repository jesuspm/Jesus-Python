# Crear una funció que mostri, per consola, i guardi en un arxiu extern, un JSON amb una key de nom book que contindrà titel, cover, year i pages.
# Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 

#Importamos la librearia de json
import json

#Aquí definimos la funcion generar_y_guardar_json()

def generar_y_guardar_json():
    datos_libros = [
        {"title": "Libro 1", "cover": "Portada1.jpg", "año": 2022, "paginas": 300},
        {"title": "Libro 2", "cover": "Portada2.jpg", "año": 2020, "paginas": 250},
        {"title": "Libro 3", "cover": "Portada3.jpg", "año": 2021, "paginas": 400},
        {"title": "Libro 4", "cover": "Portada4.jpg", "año": 2019, "paginas": 350}
    ]

    json_data = {"book": datos_libros}

    # Mostrar por consola
    print("JSON:")
    print(json.dumps(json_data, indent=2))

    # Guardar en un archivo externo
    with open("libros.json", "w") as file:
        json.dump(json_data, file, indent=2)

# Llamar a la función
generar_y_guardar_json()
