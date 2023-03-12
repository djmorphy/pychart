#Dictionaries, key-value pair- Szótárak, Kulcs értékpárokat( java-ban hash-maps, js-ben object literals

nev_kor = {'Ili':28, 'Betti':37, 'Magdi':41, 'Ani':34}

nev_kor['Andi'] = 56 #így adom hozzá Andit aki 56 éves
print(nev_kor)

print("Ili törlése!!!")
nev_kor.pop('Ili') #törlöm Ili-t
print(nev_kor)

print("Ani-nak a get-je")
print(nev_kor.get('Ani'))


#hogyan tudunk átloopolni. 3 módja van

#csak a kulcsokat szedjük ki
for key in nev_kor.keys():
    print(key)

#saját kútfő
#csak az értékek
for value in nev_kor.values():
    print(value)


#ha egyszerre akarok mindent. Az items metódus két értéket ad vissza minden iterációban
for key, value in nev_kor.items():
    print(key, value)



# a key value pair-en belül lehet szám, másik szám, lista, tuple stb
dict1 = {'adat1':[1,2,3,4,5,6], 'adat2':78, 'adat3': (9,8,7,6)}
for key, value in dict1.items():
    print(key,value)


#létrehoztam egy szótárat ami ili és ennek még egyértékpárt kor hajszín stb
nev_kor2 ={ 'Ili':{'kor':28, 'hajszin':'szoke'},
            'Betti':{'kor':37, 'hajszin':'barna'},
            'Magdi':{'kor':41, 'hajszin':'fekete'},
            'Ani':{'kor':34, 'hajszin':'voros'}}

fokok = {0:'kelet', 45:'eszak-kelet', 90: 'észak', 135:'észak-nyugat', 180:'nyugat',
         235:'dél-nyugat', 270:'dél', 315:'dél-kelet'}

