# Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
# Constructor
# Atributs (mínim 6)
# Getters/Setters
# Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
# Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json


import json

class User:
    def __init__(self, nombre, apellido, edad, correo, telefono, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    # Getters
    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_edad(self):
        return self.edad

    def obtener_correo(self):
        return self.correo

    def obtener_telefono(self):
        return self.telefono

    def obtener_direccion(self):
        return self.direccion

    # Setters
    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_apellido(self, apellido):
        self.apellido = apellido

    def establecer_edad(self, edad):
        self.edad = edad

    def establecer_correo(self, correo):
        self.correo = correo

    def establecer_telefono(self, telefono):
        self.telefono = telefono

    def establecer_direccion(self, direccion):
        self.direccion = direccion

    # Método para mostrar todos los datos del usuario
    def salutacion(self):
        print("Datos del Usuario:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")

    # Método para convertir el objeto a un diccionario (formato JSON)
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "correo": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion
        }

# Ejemplo de uso:
usuario = User("Paco", "Perez", 25, "paco@example.com", "123456789", "Calle No me acuerdo")
usuario.salutacion()
print(usuario.to_dict())
