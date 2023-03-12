"""
'r' = read
'w' = write
'a' = append (hozzáfűzés, mellékel)
"""


with open("mondasok.txt", 'r', encoding='utf-8') as infile:

#ha az out.txt nem létezik létrehozza ha létezik felülírja. Ez a komment az as infile előtt keletkezett
    with open('out.txt','w',encoding='utf-8') as outfile:

        sor = infile.readline()
        while sor:
            outfile.write(sor)
            sor = infile.readline()


with open("out.txt", 'a', encoding='utf-8') as file:
    ujsor = "nem akarásnak nyögés a vége"
    ujsor2 = '\n nem akarásnak nyögés a végeeeee'

    file.write(ujsor)
    file.write(ujsor2)

