"""
if ternary operator
if elágazásokat tudunk leegyszerűsíteni
"""

lang = "ESP"

if lang == "HUN":
    print("Jó estét")
elif lang == "ENG":
    print("Good Evening")
elif lang == "ESP":
    print("Boeno Noches")

#ez még átlátható
print("Jó estét") if lang == "HUN" else print("Good Evening")

#kezd átláthatatlan lenni
print("Jó estét") if lang == "HUN" else (print("Good Evening") if lang == "ENG" else print("Buena noches"))

