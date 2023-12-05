def nyolcas():
    beFajl = open("fajlok/szoveg.txt", "r", encoding="UTF-8")
    fajlTartalma = beFajl.read()
    # print(type(fajlTartalma))
    # print(fajlTartalma)
    beFajl.close()
    dbk = 0
    dbK = 0
    fajlTartalmaUj = ""
    for index in range(0, len(fajlTartalma), 1):
        if fajlTartalma[index] == "k":
            dbk += 1
            fajlTartalmaUj += "*"
        elif fajlTartalma[index] == "K":
            fajlTartalmaUj += "*"
        else:
            fajlTartalmaUj += fajlTartalma[index]
    print(f"Cenzúrázott fájl tartalma: {fajlTartalmaUj}")
    print(f"k betűk száma: {dbk}, K betűk száma: {dbK}.")