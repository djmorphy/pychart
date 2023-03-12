#Build in functions


#abszolult érték
print(abs(-78))


#enumarte fgv két értéket ad vissza az első az index szám a második maga a név
nevek = ['Xéna', 'Bözsi', 'Vica', 'Eni', 'Ildi', 'Zsuzsi', 'Évi']

for index, nev in enumerate(nevek):
    print(index, nev)

#átcastolja a 10-et 10.0-ra
print(float(10))

#átcastolja úgy hogy stringből szám lesz és tudok matematikai műveletet végezni
print(float('147.879'))

#szám hex száma
print(hex(125)) #return 0x7d és ebből 7d a hex szám

#ugyan úgy a string-et és átcastolja
print(int(25.78))

#lenght nem csak lista-ba hanem stringben is lehet
print(len("hello, hogy vagy?"))

#min és max
print(max(21, 2435, 543, 4))
print(min(21, 2435, 543, 4))

#hatványozás. Ugyan azt adja vissza
print(2**10)
print(pow(2,10))

#range obj ad vissza ami tartalmaz 0-tól 100ig habár sztm 99
print(range(100))
#listává konvertálás
print(list(range(100)))
#így csak 50-től kezdi ha két bemetet adok
print(list(range(50,100)))

#így stepsize-t is adok neki
print(list(range(50,100,4)))

#megfordíja a listát
print(list(reversed(nevek)))

#kerekítés
print(round(12.9524))
#mennyi számig vágja le
print(round(12.952432423, 3))

#listába kell rakni
print(sum([3,3,6,7,89,4]))

