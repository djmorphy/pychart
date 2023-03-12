

a = 10
b = 20


#itt csak kiprinteltem
def osszeadas1():
    print(a+b)

#itt visszatérési értéket használtam és a c az egy default érték
def osszeadas2(a, b, c=4):
    return a+b+c

#ha változó számú paraméter van pl egy három száz(db). Az osszeadas3 az fogadhat 0 vagy akár több paramétert is
def osszeadas3(*args):
    return sum(args)

#az args-ot nem muszáj args-nak nevezeni csak konvenció

def osszeadas4(*beka):
    return sum(beka)

def udvozlesek(*args):
    koszones = 'Ennyi féle köszönés létezik: '
    for k in args:
        koszones += k
        koszones += ", "  #ezzel adom hozzá a sapce-t és a vesszőt
    print(koszones)
    print(koszones[0:len(koszones)-2]) #-2 azert kell mert hozzá adtunk egy vesszőt és egy space-t

osszeadas1()

osszeadas2(45,25) #ez nem ír ki semmit a console-ra mert nincs print
print(osszeadas2(45,25)) #ez már kiírja
osszeg = osszeadas2(45,25) #ez tartalmazza a 70-et
print(osszeg)

print(osszeadas3(12,243,55,5432,23))
print("összeadás4()fgv")
print(osszeadas4(12,243,55,5432,23))

udvozlesek("Szia", 'Hello', 'Szevasz', 'Szervusz' 'Hali')