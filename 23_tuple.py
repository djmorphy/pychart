"""
 tuple . nem módosítható adathalmaz (angolul immutable)
 a compiler sokkal gyorsan el tudja végezni a művelteket mint a listán mivel nem módosítható
 Az egyetlen lehetőség a tuple módosításához ha új értékeket rendelünk hozzá
 pl
 tup1 = ('Juci', 'Ani', 'Ildi', 'Barbi', 'Barbi', 'Barbi')
    print(tup1)
 tup1 lista = ['Juci', 'Ani', 'Ildi', ]
    print(tup1)
"""

#módosítható adat []
lista = ['Juci', 'Ani', 'Ildi', 'Barbi']


#nem módosítható adat()
tup1 = ('Juci', 'Ani', 'Ildi', 'Barbi', 'Barbi', 'Barbi')




lista.append('Bözsi')
print(lista)
lista[-1] = 'Betti'  #utolsó elemet írd át bettire
print(lista)

# tup1[-1] = 'Betti' #hibát dob

print(tup1[2])
print(tup1[1:2])
print(tup1[1:])




#listából tuple
print('konvertálás')
tup2 = tuple(lista)
print(tup2)

print('visszakonvertálás')
lista2 = list(tup2)
print(lista2)

print('használható metódusok')
print(tup1.index('Ildi')) #mi az indexe
print(tup1.count('Barbi')) # hányszor van meg a Barbi

tup3 = ('Bettike')
print(tup3) #mivel egy eleme van ezért simán zárójelek nélkül nyomja ki mint egy stringet
print(tup3.upper()) #string miatt tudom az uppercase-t használni

