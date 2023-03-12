#pass continoue brake
"""
ha nem tudom pontosan hogy mit akar a költő akkor ezeket a placeholdereket tudom betenni és a pychart
nem fog hisztizni hogy nem jó a szintaxisom
pass-t bárhova betehetem
"""


#while True:
#    pass

#range-ben ugyan 10-et adtam meg de mivel egy if-ben megadtam hogy i értéke 5 akkor szakítsd meg a loopot
for i in range(10):
    if i == 5:
        break
    print(i)

print()
print("while ciklus")
szam = 0
while True:
    print(szam)
    if szam == 5:
        break
    szam += 1

#ha azt akarom hogy 4-ig számoljon el akkor a print(szam) után teszem a növelést
szam2 = 0
while True:
    print(szam2)
    szam2 += 1

    if szam2 == 5:
        break

print()
print("conutinue")
"""
Elszámol 0...4 |  5-öt átugorja és folytatja  |6...9
A continoue azt csinálja, hogy amikor amikor i értéke 5 lesz és megadtam azt a parancsot hogy continoue hogy minden ami
ez után következett volna pl a print átugortta és átment a következő iterációra és átment a következő loopra
"""
for i in range(10):
    if i == 5:
        continue
    print(i)


print()
print("számláló")
"""
páratlan számokat írt ki.
2-ben a 2 elfér 1szer maradék a 0. A szamlaloban a 2 ele fér úgy hogy ne legyen maradék
ha igen akkor contionue és menjünk a következő iterációra és a print(szamlalo)
"""
szamlalo = 0

while True:
    szamlalo += 1
    if szamlalo % 2 == 0:
        continue
    print(szamlalo)
    if szamlalo > 20:  #ez szakitja meg az örökös loopot
        break