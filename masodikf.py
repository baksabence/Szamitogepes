def masodik():
    lista = []
    beFajl = open("fajlok/szoveg.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    for index in range(0, len(lista), 1):
        print(lista[index], end="")
