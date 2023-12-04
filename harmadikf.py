def harmadik():
    lista = []
    beFajl = open("fajlok/szoveg.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    kiFajl = open("fajlok/negyedik.txt", "w", encoding="utf-8")
    for index in range(0, len(lista), 1):
        print(lista[index], file=kiFajl, end="")
        #kiFajl.write(lista[index])
    kiFajl.close()