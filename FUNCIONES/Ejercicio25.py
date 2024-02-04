# Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
# Constructor
# Atributs (mínim 6)
# Getters/Setters
# Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
# Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

import json

class Vehiculo:
    def __init__(self, marca, modelo, año, color, tipo_combustible, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_combustible = tipo_combustible
        self.kilometraje = kilometraje

    # Getters
    def obtener_marca(self):
        return self.marca

    def obtener_modelo(self):
        return self.modelo

    def obtener_año(self):
        return self.año

    def obtener_color(self):
        return self.color

    def obtener_tipo_combustible(self):
        return self.tipo_combustible

    def obtener_kilometraje(self):
        return self.kilometraje

    # Setters
    def establecer_marca(self, marca):
        self.marca = marca

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def establecer_año(self, año):
        self.año = año

    def establecer_color(self, color):
        self.color = color

    def establecer_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def establecer_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    # Método para mostrar todas las partes del vehículo
    def mostrar_partes(self):
        print("Partes del Vehículo:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Kilometraje: {self.kilometraje}")

    # Método para convertir el objeto a un diccionario (formato JSON)
    def a_diccionario(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "año": self.año,
            "color": self.color,
            "tipo_combustible": self.tipo_combustible,
            "kilometraje": self.kilometraje
        }
#Aquí probamos imprimimos todo.
vehiculo = Vehiculo("Toyota", "Camry", 2022, "Azul", "Gasolina", 15000)
vehiculo.mostrar_partes()
print(vehiculo.a_diccionario())






