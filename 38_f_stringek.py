#String formátozás, es f stringek

#régi mód. %s az string %d az meg digit
szoveg1 = "A te neved %s, és %d eves vagy." % ("Andi", 37)
print(szoveg1)


#nem olyan régi mód. (Format metódus)
szoveg2 = "A te neved {}, és {} eves vagy.".format("Ildi", 28)
print(szoveg2)

#új mód (f string)
nev = "Enikő"
kor = 35
szoveg3 = f"A te neved {nev}, és {kor} éves vagy."
print(szoveg3)
print()
print("for ciklus")
nevek_szotar = {"Betti":28, "Evi":32, "ildi":31, "Zsuzsi":40, "Andi":34}

for nev,kor in nevek_szotar.items():
    print(f"A te neved {nev}, és {kor} éves vagy.")
    print(f"A te neved {nev}, és {kor+4} éves vagy.")  #mindenki 4 évevel idősebb
