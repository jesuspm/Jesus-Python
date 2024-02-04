import xml.etree.ElementTree as ET #ET es el alias que nosotros definimos, podria llamarse paco o fermin.

def crear_xml():
    # Aquí creamos el elemento root
    root = ET.Element("students")

    # Creamos cinco elementos child "student"
    for i in range(1, 6):
        student = ET.SubElement(root, "student")

        # Creamos cuatro subchilds en cada elemento "student"
        name = ET.SubElement(student, "name")
        surname = ET.SubElement(student, "surname")
        email = ET.SubElement(student, "email")
        dni = ET.SubElement(student, "dni")

        # Añadimos un atributo a cada elemento "student"
        student.set("id", f"{i}")

        # Insertar texto en cada subchild
        name.text = f"Nombre{i}"
        surname.text = f"Apellido{i}"
        email.text = f"email{i}@dominio.com"
        dni.text = f"1234567{i}"

    # Crear el árbol XML
    tree = ET.ElementTree(root)

    # Escribir el árbol XML en un archivo
    tree.write("students.xml")

    # Mostrar el contenido del archivo por consola
    with open("students.xml", "r") as file:
        contenido_xml = file.read()
        print(contenido_xml)

# Llamar a la función para crear el XML
crear_xml()
