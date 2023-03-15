# "is" "is not" identity operator = azonossági operátpr
"""két változó ugyan arra az objektumra mutat-e? """

szam1 = 4
szam2 = 4

print(szam1 == szam2) #kapok egy true-t

szam = 8


if type(szam) is int:
    print("int típus")
if type(szam) is not str:
    print("nem string")

szam = "8"  #így már string

if type(szam) is not int:
    print("nem int típus")

igaz = True

print(type(igaz) is bool)
print(type(igaz) is not bool)


class Szemely:
    pass

sz1 = Szemely()

sz2 = Szemely()

if type(sz1) is Szemely:
    print("Személy típus")
else:
    print(type(sz1))

if type(sz1) is int:
    print("Személy típus")
else:
    print(type(sz1))

print(sz1 is sz2) #false-t ad. Nem azt hasonlítja össze hogy az sz1 és sz2 u.a. típus-e hanem sz1 sz2 ugyan arra objektumra mutat-e


sz3 = Szemely()
sz4 = sz3

print(sz3 is sz4) #így már true


if isinstance(sz1, Szemely):   #isistance megnézi hogy az sz1 személy típus-e
    print("Személy típus")
