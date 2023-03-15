# "in" membership operator - tagsagi operator

mondas = "Bagoly mondja verébnek, hogy nagyfejű."

for betu in mondas:
    print(betu)

print("Bagoly" in mondas) #boolean-t ad vissza
print("fekcse" in mondas) #boolean-t ad vissza

if "Bagoly" in mondas:
    print("találat!")


nevek_lista = ["Betti", "Evi", "Ildi", "Zsuzsi", "Andi"]

if "Evi" in nevek_lista:
    print("Találat a nevek listában!")

if "Klári" not in nevek_lista:
    print("Nincs találat")


nevek_szotar = {"Betti":28, "Evi":32, "ildi":31, "Zsuzsi":40, "Andi":34}

if "Ildi" in nevek_szotar:
    print("találat")

# nincs találtad mert csak kulcsok alapján keres
if "28" in nevek_szotar:
    print("találat")

if "Klári" not in nevek_szotar:
    print("nincs találat")

szamok1 = [1, 2, 3, 4, 5, 6, 7]
szamok2 = [0, 2, 6, 8, 7]

#össze akarom hasonlítani melyik azok ami megvan mint két listában

azonos_szamok = []
egyedi_szamok = []
for szam in szamok1:
    if szam in szamok2:
        azonos_szamok.append(szam)
    else:
        egyedi_szamok.append(szam)

"""        
#nicns meg mit a két listában #sajat iq de else ágat megírni egyszerűbb lett volna...
for szam in szamok1:
    if szam not in szamok2:
        egyedi_szamok.append(szam)
"""
print(azonos_szamok)
print(egyedi_szamok)
#refaktor csak kikommentelni kellene a masik loopot
for szam in szamok1:
    if szam not in szamok2:
        egyedi_szamok.append(szam)

print()
print(egyedi_szamok)
