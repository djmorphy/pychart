"""
    stringek - karakterláncok
    concatenation - összefűzés
    slicing - szeletelés
    indexing - idexelés
    len() - string hossz azaz karakter szám

"""


szoveg = "Az én csajom Anna és 39 éves"
print(szoveg)

szoveg = szoveg.replace("Anna", "Gyöngyi")
print(szoveg)

szoveg = szoveg.replace("Gyöngyi", "Mucus").replace("39","22")
print(szoveg)

szoveg = szoveg.replace("Mucus", "Mucika").replace("22","38") + " Nagyon szeretem :)"
print(szoveg)

print(szoveg.index("Mucika"))
print(len(szoveg))
print(szoveg.startswith("Az")) #Ez a szöveg "Az"-al kezdődik és booleant ad vissza
print(szoveg.endswith("Őt")) #ez a vége boolean-al. Azért false mert smile a vége

print(szoveg[13:13+4])   # 13 karaktertől printeld ki a 13+4-et
print(szoveg[13:17]) #ugyan az mint a fölötte lévő
print(szoveg[-2:]) # a végétől az utolsó 2 karaktert printeld ki

szoveg2 = "             Ma este iszom egy korsó sört.           "
print(szoveg2)
print(szoveg2.lstrip()) #leftről levágja a sapcet
print(szoveg2.rstrip())  #right-ről levágom
print(szoveg2.strip()) #jobbról és balról levágom a space-t


adatok1 = "0,1,2,3,4,5,6,7,8,9"
adatok1 = adatok1.split(",")
print(adatok1)

adatok2 = "Eni;Zsoka;Andi;Reka;Zsuzsi"
adatok2 = adatok2.split(";")
print(adatok2)
