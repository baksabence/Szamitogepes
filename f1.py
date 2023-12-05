def osztalyBeir():
    kiFajl = open("fajlok/proba.txt", "a", encoding="UTF-8")
    kiFajl.write("\ntanuló")
    kiFajl.close()

    def kiir():
        beFajl = open("fajlok/proba.txt", "r", encoding="UTF-8")
        adatok = beFajl.read()
        print(adatok)
        beFajl.close()

        beFajl = open("fajlok/proba.txt", "r", encoding="UTF-8")
        adatok = beFajl.readline()
        print(beFajl.readline())
        beFajl.close()

        beFajl = open("fajlok/proba.txt", "r", encoding="UTF-8")
        elso5 = beFajl.read(5)
        print(elso5)
        beFajl.close()