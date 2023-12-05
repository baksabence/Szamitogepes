"""
import Szamitogep

szg1 = Szamitogep.Szamitogep(0, False)
szg2 = Szamitogep.Szamitogep(0, False)

szg1.kapcsol()
if szg1.programMasol(800):
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")
if szg1.programMasol(400):
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")

if szg2.programMasol(1):
    print("A másolás sikeres volt")
else:
    print("A másolás sikertelen volt")

print(szg1)
print(szg2)

"""""
# import f1
# import f2
# import Csoport
# import elsof
# import masodikf
# import harmadikf
# import negyedikf
# import hetesf
# import nyolcasf
# import tizenkettesf
# import f1
# import f2
import Csoport

# elsof.elso()
# masodikf.masodik()
# harmadikf.harmadik()
# negyedikf.negyedik()
# hetesf.hetesf()
# nyolcasf.nyolcas()
# tizenkettesf.tk()
# f1.osztalyBeir()
# f2.masodik()

adatokListaja = []


def beolvasas():
    beFajl = open("fajlok/csoport.txt", "r", encoding="UTF-8")
    beFajl.readline()
    sorok = beFajl.readlines()

    for sor in sorok:
        tisztitottsor = sor.strip()
        print(tisztitottsor)
        daraboltsor = tisztitottsor.split("/")
        print(daraboltsor)
        csoporttag = Csoport.Csoport(daraboltsor[0], daraboltsor[1], daraboltsor[2])
        print(csoporttag)
        adatokListaja.append(csoporttag)
    beFajl.close()

def sorokSzama():
    sorszam = len(adatokListaja)
    print(f"A tanulók száma: {sorszam}.")


def megszamlalas():
    osszeg = 0
    for index in range(0, len(adatokListaja), 1):
        osszeg += adatokListaja[index].atlag

    if len(adatokListaja) == 0:
        atlag = 0
    else:
        atlag = osszeg/len(adatokListaja)
    print(f"A suli átlag: {atlag}.")

def elsosokSzama():
    db = 0
    for index in range(0, len(adatokListaja), 1):
        if adatokListaja[index].evfolyam == 1:
            db += 1
    print(f"Az elsősök száma: {db}")


beolvasas()
sorokSzama()
megszamlalas()
elsosokSzama()