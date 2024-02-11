#delete
from connection import cursor, conn

# Consulta SQL para eliminar un usuario
sql = "DELETE FROM public.users WHERE user_id = %s;"

# Solicitamos al usuario que ingrese el ID del usuario que quiere eliminar
user_id = input("Introduce el ID del usuario que quieres eliminar: ")

# Recopilamos los datos
datos = (user_id,)

try:
    # Utilizamos el método execute para ejecutar la consulta SQL con los datos proporcionados
    cursor.execute(sql, datos)

    # Con cursor.rowcount contamos el número de filas afectadas por la consulta DELETE
    eliminacion = cursor.rowcount
    
    # Confirmamos los cambios en la base de datos
    conn.commit()

    if eliminacion == 1:
        # Mostramos el resultado
        print(f'Usuario con ID {user_id} eliminado exitosamente.')
    else:
        print("No se encontró ningún usuario con ese ID.")

except Exception as e:
    # Si ocurre algún error, imprimir el mensaje de error
    print(f"Error al eliminar usuario: {e}")
finally:
    # No olvides cerrar el cursor y la conexión después de usarlos
    cursor.close()
    conn.close()
