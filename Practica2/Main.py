import psycopg2
from connection import *

try:

except(Exception, psycopg2.Error) as error:
    print("Error:", error)
finally:
    conn.close()