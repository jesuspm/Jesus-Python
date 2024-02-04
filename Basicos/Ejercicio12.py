# Crear una tupla amb els mesos de l’any. 
# Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per pantalla el mes corresponent al número indicat per l’usuari. 
# El programa finalitza només quan l’usuari posa 0.
meses = ("enero","febrero","marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre" , "diciembre")


numero = int(input("Introduce un numero entra el 1 y el 12 para saber el mes: "))
if 1<= numero <=12:

    tuplaMeses = meses[numero]
    print("El numero -> " + str(numero) + "corresponde al mes --> " + str(tuplaMeses))

else:
    print("Error,el numero introducido no equivale a ningún mes del año.")
