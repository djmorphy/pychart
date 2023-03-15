

with open("egyeb/Matild.txt", "r", encoding="utf-8") as in_file:
    szoveg = ""

    sor = in_file.readline()

    while sor:
        szoveg += sor.lstrip().replace("Matild","Ildikó").replace(", marha","")

        sor = in_file.readline()

    with open("egyeb/Ildiko.txt", "w", encoding="utf-8") as out_file:
        out_file.write(szoveg)

    print(szoveg)

