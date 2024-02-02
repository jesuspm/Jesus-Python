#Demanar a l’usuari un nùmero entre 10 i 100.
#Posar els números a una tupla desde 1 fins al número indicat per l’usuari.
#Exemple: usuari indica 34, es crea una tupla i es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).

# Demanar a l'usuari un número entre 10 i 100
numero_usuari = int(input("Introdueix un número entre 10 i 100: "))

# Verificar que el número està dentro del rango
if 10 <= numero_usuari <= 100:
    # Crear la tupla con el numero del 1 al que indique el usuario, el +1 es para que le sume 1 a la tupla ya que comienza por la posicion 1 en vez de la 0.
    tupla_numeros = tuple(range(1, numero_usuari +1))

    # Imprimir la tupla
    print("La tupla amb els números de l'1 al", numero_usuari, "és:")
    print(tupla_numeros)
else:
    print("El número no està dins del rang permès.")
