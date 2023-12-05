def masodik():
    beFajl = open("fajlok/tetszoleges.txt", "r", encoding="UTF-8")
    beFajl.readline()
    print(beFajl.readline())
    beFajl.close()

    kiFajl = open("fajlok/tetszoleges.txt", "a", encoding="UTF-8")
    kiFajl.write("\nnegyedik")
    kiFajl.close()

    beFajl = open("fajlok/tetszoleges.txt", "r", encoding="UTF-8")
    print(beFajl.read())
    beFajl.close()

