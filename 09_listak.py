#list (mutable - listák (modosíthatók)
#lista az lehet több típsú nem úgy mint a JAVA-ban hogy az int az csak int lehet
lista1 = []

print(lista1)


#lista feltöltése
lista1.append(100)
lista1.append(101)
lista1.append(102)
lista1.append(103)
lista1.append(104)

print(lista1)


lista1.append("Enikő")
lista1.append("Anikó")
lista1.append("Enikő")
print(lista1)


#lista elem eltávolítása
lista1.remove("Enikő")
print(lista1)

#5. poziba elemet berakni
lista1.insert(5,"Bözsi")
print(lista1)

#lista elemek megfordítása
lista1.reverse()
print(lista1)

#teljes lista ürítése
lista1.clear()
print(lista1)


#értékkekel inicializálás
lista2 = [15, 8, 78, 23, 1, 65, 184]

#szortirozás növekvő sorrendbe. Csak akkor tudom használni ha csak számból vagy csak szövegből áll
lista2.sort()
print(lista2)

#szortirozás abc szerint
lista3 = ["Xéna", "Bözsi", "Eni", 'Ildi', 'Vica']
lista3.sort()
print(lista3)

alpha = [ 'r','c','f','d', 'o','l','q','i','x','h','u','j','k','w','m','v','y','b','g','p','a','e','t','n','s']
alpha.sort()
print(alpha)

#ezt az ötletet az előző trainingből vettem hogy összekombózom
print(f"Az alpha listában {len(alpha)} db betű van!")




