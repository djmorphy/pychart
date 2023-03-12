#for loop - for ciklus

#10-szer írom ki a hello-t
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('Hello')
print('')

#for loop-al
# i az az iterátror rövidítésből jön
for i in range(10):
    print('Hello for loopal')
    print('Bello for loopal')

#0-9ig kiírja
for bla in range(10):
    print(bla)

tartomany = range(100)
print(tartomany)
print()
print("Listává konvertálás")
print(list(tartomany))



lista1 = ['Xena', 'Bözsi', 'Vica', 'Eni', 'Ildi']
print("listának ennyi eleme van:")
print(len(lista1))
print()
"""
5 elem van alistában. Ha végig akarok loopolni rajta. Listát az i-diknél indexelem. Az i elsőnek nulla lesz ami Xena-ra mutat
majd a következ iterációban 1-es lesz ami már a bözsire mutat és mindig kiírja a Lista1-et az i-dik indexnél
Itt a range fgv-t használtam amivel megadtam a lista hosszát 
"""
for i in range (len(lista1)):
    print(lista1[i])


#for each loop ami ugyan úgy működik mint a fenti interációs
"""
az i mindig vegye fel a listából az elemeknek az értékét.
Az első iterációban az i értéke Xena majd kiprintelem. Köv iterációban az i értéke Bözsi majd kiprintelem
"""
print("For each loopal")
for i in lista1:
    print(i)


