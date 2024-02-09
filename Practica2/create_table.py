from connection import *
#Se crea la tabla users a la BDD
sql = """CREATE TABLE USERS(
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_surname VARCHAR(255) NOT NULL,
                user_age BIGINT NOT NULL,
                user_email VARCHAR(255) NOT NULL
)"""

print(sql)
# Con el metodo execute() se envia la query
connection.execute(sql)
print(connection)
# commit para hacer efectivos los cambios de la query a la BDD
conn.commit()