"""
    classes and the objects oriented programing - osztalyok es az objektum orientált programozás
    user define types - felhasználó által definiált tipusok

az __init__ metodus mas nyelveken ez a konstrutor metódus
Azért kell mert amikor létregozom az Ildi -t akkor a zárójelben néhány iniciális paramétert pl név, kor stb)
megadhassak
Ez az __init__ metódus automatikusan lefut amikor az objektum példányt létrehozzuk
"""

class Szemely:
    def __init__(self, nev, kor, neme, nemzetiseg, vallas='hindu'):
        self.nev = nev
        self.kor = kor
        self.neme = neme
        self.nemzetiseg = nemzetiseg
        self.vallas = vallas
        # Ha van egy csomó obj amin nem akarom egyesével meghívogatni a hello-t
        self.hello()

    def hello(self):
        print('Hello ' + self.nev )

Ildi = Szemely('Ildikó', 32, 'nő', 'magyar', 'keresztény') #ez az inicializálás
Laci = Szemely('László', 47, 'férfi', 'Kínai')

print(Ildi.vallas)
print(Laci.vallas)

#Ildi.hello()  #mert meghivtam az init-ben a self.hello() -t és nem kell egyesével
#Laci.hello()

print(type(Ildi))
print(type(Laci))

