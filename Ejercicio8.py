#Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es
#indicada/es per l’usuari, indicar quants caràcters té i indicar el primer, i l’últim caràcter.


paraula1 = input("Introduce la primera palabra: ")

paraula2 = input("Introduce la segunda palabra: ")

paraula3 = input("Introduce la tercera palabra: ")

#Muestra las 3 palabras.
print("Las tres palabras introducidas por el usuario son: " + "1-" +paraula1 + " " + "2-" + paraula2 + " " + "3-" + paraula3)

#Indica cuantos carácteres tiene cada palabra.
print("La primera palabra que es --> " + paraula1 + ", contiene --> " + str(len(paraula1)) + " caracteres")
print("La segunda palabra que es --> " + paraula2 + ", contiene --> " + str(len(paraula2)) + " caracteres")
print("La tercera palabra que es --> " + paraula3 + ", contiene --> " + str(len(paraula3)) + " caracteres")

#indicar el primer y el últim caracter.
print("El primer y último carcater de --> " + paraula1 + " es --> " + paraula1[0] + " y " + paraula1[-1])
print("El primer y último carcater de --> " + paraula2 + " es --> " + paraula2[0] + " y " + paraula2[-1])
print("El primer y último carcater de --> " + paraula3 + " es --> " + paraula3[0] + " y " + paraula3[-1])














