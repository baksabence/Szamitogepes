def hetesf():
    lista = []
    beFajl = open("fajlok/szoveg.txt", "r", encoding="UTF-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    kiFajl = open("fajlok/negyedik.txt", "w", encoding="UTF-8")
    for index in range(len(lista)-1, -1, -1):
        print(lista[index])
        print(lista[index], file=kiFajl)
        # kiFajl.write(lista[index])
    kiFajl.close()