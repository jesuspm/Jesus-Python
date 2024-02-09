#Insert 
from connection import *


#Utilizaremos el metodo cursor() para hacer la conexión.
connection = conn.cursor()

# El try intenta ejecutar el insert
try:
    sql="INSERT INTO public.users(user_name, user_surname, user_age, user_email) VALUES (jesus,pujada,25,jpujada30@gmail.com)"
    connection.execute()  # Confirmamos la insert
    print("Inserción exitosa")
    
except Exception as e:
    print(f"Error al insertar datos: {e}")

# Cerrar conexión
connection.close()
