def elso():
    beFajl = open("fajlok/szoveg.txt", "r", encoding="utf-8")
    for sor in beFajl:
        print(sor.strip(), end=" ")
    beFajl.close()