# Demanar a l’usuari que introdueixi 10 números separats per un espai. Al acabar, el programa els introduirà en una 
# tupla i els ordenarà (major o menor, com volgueu), mostrant per pantalla el contingut de la tupla.

tst = False
while tst == False:
    entradaNumeros = input("Ingresa 10 valores separados por espeacio: ")
    test = entradaNumeros.split(" ")
    if (len(test) == 10):
        tst = True
    else:
        print("Error, tienes que introducir 10 valores.")
tuplaNums = tuple(map(int, test))

resultado = sorted(tuplaNums)

print("Tupla actualizada:", str(resultado))
