"""
a metódusok egyfajta fgv-nyek különbség de különbséga normál fgv és metódusok között
hogy a metódust osztályban definiáljuk. Tehát a metódus az ami egy osztályból létrehozott
objektumon hajt végre műveleteket

"""

class Szemely:
    neve =''
    kor = None
    neme =''
    hajszin = ''

    # methods
    def set_kor(self, value):
        # kor=value # Ez a kor nem az a kor ami a Szemely osztály mezőjében van. Ezért kell elé a self
        self.kor = value
    def set_nev(self, value):
        self.neve = value

    def set_neme(self, value):
        self.neme = value

    #saját kutfő
    def set_haj(self, value):
        self.hajszin = value

#object instance - objektum példány
Ili = Szemely()
Ili.set_nev('Ili')
Ili.set_kor(21)
Ili.set_neme('nő')
Ili.set_haj('dögös vörös')


print(Ili.kor)
print(Ili.neve)
print(Ili.neme)
print(Ili.hajszin)


Laci = Szemely()

Laci.set_kor(48)
Laci.set_nev("Laci")
Laci.set_neme('Férfi')
Laci.set_haj('Kopasz')

print(Laci.neve)
print(Laci.kor)
print(Laci.neme)
print(Laci.hajszin)