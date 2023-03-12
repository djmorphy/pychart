

jelszo = 'kisuborka'

bemenet = input('Mi a jelszó? ')
proba = 0

while bemenet != jelszo:
    proba += 1
    if proba == 3:
        print("BANNOLTALAK")
        break
    print("rossz jelszó, próbáld újra")
    bemenet = input('Mi a jelszó? ')

if bemenet == jelszo:
    print("sikeres belépés a nukleáris indítókódokhoz")
