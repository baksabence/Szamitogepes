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

#import elsof
#import masodikf
#import harmadikf
import negyedikf
import hetesf

#elsof.elso()
#masodikf.masodik()
#harmadikf.harmadik()
negyedikf.negyedik()
hetesf.hetesf()