#super() function - super függvény

""""
alkalmazott osztályon belül is létre akarok hozni egy konstruktort
Ha az alkalmazott osztályban létrehozok egy __init__ metódust akkor azon belül
meg kell hívnom a super osztályt ez esetben a Személy(): __init__ metódusát
Amikor a super () osztályt akkor már nem kell a self!!!!
"""

class Személy:
    def __init__(self, nev, kor, neme, nemzetiseg, vallas='hindu'):
        self.nev = nev
        self.neme = neme
        self.nemzetiseg = nemzetiseg
        self.vallas = vallas
        self.hello()

    def hello(self):
        print('Hello' + self.nev)

class Alkalmazott(Személy):
    def __init__(self, nev, kor, neme, nemzetiseg, vallas,tapasztalat,megbizhatosag,vegzettseg):
        super().__init__(nev, kor, neme, nemzetiseg, vallas)
        self.tapasztalat = tapasztalat
        self.megbizhatosag= megbizhatosag
        self.vegzettseg = vegzettseg

#object instance - példányosítás
Eni = Alkalmazott('Enikő', 25, 'nő', 'Magyar', 'pogány', 8, 8, 'könyvelő')
Kinga = Alkalmazott('Kinga', 36,'nő', 'Magyar','protestans', 12, 7.5, 'informatikus' )

print(Eni.nev)
print(Eni.vegzettseg)
print(Eni.vallas)

print(Kinga.nev)
print(Kinga.vegzettseg)
print(Kinga.vallas)