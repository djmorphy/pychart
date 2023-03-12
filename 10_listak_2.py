


lista1 = ['Xena', 'Bözsi', 'Vica', 'Eni', 'Ildi']

print(lista1)

#indexelés
#sakat qútfő és juppi
print(lista1[3])

#foggd meg az utolsó elemet és azt add vissza
#print(lista1[-1])
print(f"utlsó elem: {lista1[-1]}")




#szeletelés. Xenia és Bözsi.  Nem inklúziv azaz a menj a 2-ig de a 2 már nincs benne
print(lista1[0:2])

#ildi nincs benne
print(lista1[2:4])

#Bözsitől akarom végig kiírni
print(lista1[1:])


#multi dimenzios listak

lista2 = [[1,2,3], [4,5,6], [7,8,9]]  #2 dimenziós lista

#full lista print
print(lista2)

print(lista2[0]) #0 index az 1,2,3  az 1index az a 2,3,4 stb

#második lista első index ami a 8
print("Második lista első index:")
print(lista2[2][1])

""" ITERÁTOR"""
#létrehozok egy listát 0-tól 99-ig mert nem inkluzív
tartomany = range(100)

print(tartomany)

print(list(tartomany))  #átkonvertálom listává