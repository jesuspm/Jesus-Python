# Importar conexión desde el módulo connection
from connection import *

# El try intenta ejecutar el insert

# Usar comillas simples para los valores de texto y comillas dobles para la consulta SQL
sql = "INSERT INTO public.users(user_name, user_surname, user_age, user_email) VALUES ('MIREYA', 'SANCHEZ', 22, 'jpujada30@gmail.com')"

# Ejecutar la consulta SQL
cursor.execute(sql)

# Confirmar la inserción
conn.commit()

cursor.close()
print("Inserción exitosa")
