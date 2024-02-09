import psycopg2
from connection import *
from create_table import *

opciones = input("Ingresa la opcion que quieras ejecutar: ")
try:
    print("Opcion:1 -> Crear Tabla")
    opcion1 = connection.execute(sql)
    
    print("Opcion:2 -> Modificar Tabla")
    print("opcion:3 -> Upgrade Tabla")
    print("opcion:4 -> Delete Tabla")
    
#hacer un menu con opciones para elegir que es lo que quieres hacer
except(Exception, psycopg2.Error) as error:
    print("Error:", error)
finally:
    conn.close()