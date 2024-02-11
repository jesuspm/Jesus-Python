from connection import cursor, conn

# Consulta SQL para actualizar los datos de un usuario
sql = "UPDATE public.users SET user_name=%s, user_surname=%s, user_age=%s, user_email=%s WHERE user_id=%s;"

# Solicitamos al usuario que ingrese los nuevos datos
user_id = input("Introduce el ID del usuario que quieres actualizar: ")
user_name = input("Introduce el nuevo nombre: ")
user_surname = input("Introduce el nuevo apellido: ")
user_age = input("Introduce la nueva edad: ")
user_email = input("Introduce el nuevo correo electrónico: ")

# Recopilamos los datos
datos = (user_name, user_surname, user_age, user_email, user_id)

try:
    # Utilizamos el método execute para ejecutar la consulta SQL con los nuevos datos
    cursor.execute(sql, datos)

    # Con cursor.rowcount contamos el número de filas afectadas por la consulta UPDATE
    actualizacion = cursor.rowcount
    
    # Confirmamos los cambios en la base de datos
    conn.commit()

    if actualizacion == 1:
        # Mostramos el resultado
        print(f'Registro actualizado: {actualizacion}')
    else:
        print("Error al actualizar")
except Exception as e:
    # Si ocurre algún error, imprimir el mensaje de error
    print(f"Error al actualizar datos: {e}")
finally:
    #cerramos el cursor y la conexión después de usarlos
    cursor.close()
    conn.close()
