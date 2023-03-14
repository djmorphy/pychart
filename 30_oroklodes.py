#user defined types - felhasznalo által definiált típusok

#inheritance = öröklődés

class Személy:
    def __init__(self, nev, kor, neme, nemzetiseg, vallas='hindu'):
        self.nev = nev
        self.kor = kor
        self.neme = neme
        self.nemzetiseg = nemzetiseg
        self.vallas = vallas
        # Ha van egy csomó obj amin nem akarom egyesével meghívogatni a hello-t
        self.hello()

    def hello(self):
        print('Hello ' + self.nev)


"""
class Alkalmazott(Személy):
ez a syntax. Így hogy zárójelbe van már az összess tulajdonságát örökölte a Személy(): -nek
A Személy(): az a szupter osztálya az Alkalmazottnak():
"""
class Alkalmazott(Személy):
    tapasztalat = 4
    megbizhatosag = 8
    vegzettseg = 'könyvelő'

#object instance - plédányosítás

Eni = Alkalmazott('Enikő', 25, 'Nő', 'Magyar', 'pogány')
Kinga = Alkalmazott('Kinga', 33, 'Nő', 'Német', 'ateista')


print(Eni.nev)
print(Eni.vegzettseg)

Kinga.vegzettseg ='Informatikus'
print(Kinga.nev)
print(Kinga.vegzettseg)
print(Kinga.vallas)