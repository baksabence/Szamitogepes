def negyedik():
    lista = []
    beFajl = open("fajlok/szoveg.txt", "r", encoding="UTF-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    kiFajl = open("fajlok/negyedik.txt", "w", encoding="UTF-8")
    for index in range(0, len(lista), 1):
        daraboltSor = lista[index].split(" ")
        print(daraboltSor[0], file=kiFajl)
        # kiFajl.write(lista[index])
    kiFajl.close()