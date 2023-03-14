"""
    classes and the objects oriented programing - osztalyok es az objektum orientált programozás
    user define types - felhasználó által definiált tipusok
csoportosítani tudok adatokat és metódusokat logikus módon osztályokba

"""


class Szemely:
    #member varriables/fields - tag változók/mezők
    neve =''
    kor = None
    neme =''

sz1 = Szemely
sz1.neve = 'Ildi'
sz1.kor = 28
sz1.neme = 'nő'

print(sz1.neve)
print(sz1.kor )
print(sz1.neme)

sz2 = Szemely
sz2.neve = 'Laci'
sz2.kor = 48
sz2.neme = 'férfi'

print(sz2.neve)
print(sz2.kor )
print(sz2.neme)

