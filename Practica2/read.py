#select
from connection import *

#Realizamos un select que nos devolverá toda la tabla users.
sql = "SELECT * FROM public.users"

#Ejecutamos la consulta sql 
cursor.execute(sql)

mostrarQuery = cursor.fetchall();

print(mostrarQuery)

cursor.close()

print("Select realizado con exito.")
