
nevek1 = ['Xéna', 'Bözsi', 'Vica', 'Eni', 'Ildi', 'Zsuzsi', 'Évi', 10, True]
nevek2 = ['Pityu', 'Ati', 'Peti', 'Bence', 'Feri']


for nev in nevek1:
    print(nev)

for nev in nevek2:
    print(nev)

def nev_printer(nev_lista):
    for nev in nev_lista:
        print(nev)
def nev_upper(nev_lista):
    for nev in nev_lista:
        if isinstance(nev, str): #ha ez nincs és a nevek1-hez hozzá adok egy számot akkor atributError lesz de ez megkérdezi hogy ez string-e ha igen írd ki
            print(nev.upper())
        else:
            print("nem string típus hanem: " + str(type(nev)))
#fgv meghivás vagy invokáció. Function calling/Function invocation

print()
print("névprinter meghívása")
nev_printer(nevek1)
nev_printer(nevek2)

print("saját kútfő")
nev_upper(nevek1)