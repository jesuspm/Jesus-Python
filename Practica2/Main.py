from connection import cursor, conn

def crear_tabla():
    nombre_tabla = input("Ingrese el nombre de la tabla: ")
    try:
        # Lógica para crear la tabla usando el nombre proporcionado
        sql = f"""CREATE TABLE {nombre_tabla} (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(255) NOT NULL,
                    user_surname VARCHAR(255) NOT NULL,
                    user_age BIGINT NOT NULL,
                    user_email VARCHAR(255) NOT NULL
        )"""
        cursor.execute(sql)
        conn.commit()
        print(f"Tabla '{nombre_tabla}' creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la tabla '{nombre_tabla}': {e}")

def modificar_tabla():
    nombre_tabla = input("Ingrese el nombre de la tabla que desea modificar: ")
    opcion = input("Seleccione qué desea hacer: (A)gregar columna, (E)liminar columna, (M)odificar tipo de datos: ").upper()
    if opcion == "A":
        nombre_columna = input("Ingrese el nombre de la nueva columna: ")
        tipo_datos = input("Ingrese el tipo de datos de la nueva columna: ")
        try:
            sql = f"ALTER TABLE {nombre_tabla} ADD COLUMN {nombre_columna} {tipo_datos};"
            cursor.execute(sql)
            conn.commit()
            print(f"Columna '{nombre_columna}' agregada exitosamente a la tabla '{nombre_tabla}'.")
        except Exception as e:
            print(f"Error al agregar columna: {e}")
    elif opcion == "E":
        # Lógica para eliminar columna
        pass
    elif opcion == "M":
        # Lógica para modificar tipo de datos de columna
        pass
    else:
        print("Opción inválida.")

def actualizar_tabla():
    # Implementa la lógica para actualizar la tabla
    pass

def eliminar_tabla():
    nombre_tabla = input("Ingrese el nombre de la tabla que desea eliminar: ")
    confirmacion = input(f"¿Está seguro que desea eliminar la tabla '{nombre_tabla}'? (S/N): ").upper()
    if confirmacion == "S":
        try:
            sql = f"DROP TABLE {nombre_tabla};"
            cursor.execute(sql)
            conn.commit()
            print(f"Tabla '{nombre_tabla}' eliminada exitosamente.")
        except Exception as e:
            print(f"Error al eliminar la tabla '{nombre_tabla}': {e}")
    else:
        print("Operación cancelada.")

def salir():
    print("Saliendo del programa.")

# Resto del código del menú...

