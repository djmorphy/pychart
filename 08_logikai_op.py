#logikai operátorok
#and or not  Megj.: Java-ban && || !
"""
            Magamnak a logikai értékek
True and True = True
True and False = False
False and True = False
Fals and False = False

True or True = True
True or False = True
False or True = True
False or False = False


True and not False = True
"""

szam1= 2
szam2 = 4


print(szam1 < szam2 and szam1 == 2)
print(szam1 < szam2 and szam1 == 3)
print(szam1 < szam2 or szam1 == 3)
print(szam1 < szam2 or szam1 == 3 or 5 > 6) #true lesz

print(szam1 < szam2 and not szam1 == 3) #true


