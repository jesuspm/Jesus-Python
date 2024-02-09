import psycopg2


conn = psycopg2.connect(
    database="postgres",
    user='admin',
    password='admin',
    host='localhost',
    port='5432'
)

#Utilizaremos el metodo cursor() para hacer la conexión.
connection = conn.cursor()

