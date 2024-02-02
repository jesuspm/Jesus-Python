# Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà en una 
# tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.


entradaNumeros = input("Ingresa 10 valores separados por espeacio: ")

test = entradaNumeros.split();

resultador = test.sorted(test);

print("Tupla actualizada:", str(resultador))
