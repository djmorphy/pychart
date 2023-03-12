
#mi a file neve, következő paraméter hogy read vagy write és karakterkódolás
file = open('mondasok.txt', 'r', encoding='utf-8')
""" 
#elsősor
sor = file.readline()
print(sor)

#második sor
sor = file.readline()
print(sor.strip()) #nincs new line

#harmadik sor
sor = file.readline()
print(sor.strip())
"""


"""
print()
print("for loopal")
for sor in file:
    print(sor.strip())
    
file.readLine() egy sort olvas be
file.readLines() listába rakja a sorokat. A lista első eleme az első sor
file.read egyszerre beolvassa az egész file-t. Pl xls-t amibe 6 millió sor van nem kellene így

"""
print()
print("while ciklussal")

sor = file.readline() # muszáj beolvasni először valamit
while sor:
    print(sor.strip())
    sor = file.readline()

file.close()

print()
print()


#context managerrel. Itt nem kell close mert magától lezárja
print("context managgerrel")
with open('mondasok_2.txt', 'r', encoding='utf-8' ) as file:
    for sor in file:
        print(sor.strip())

