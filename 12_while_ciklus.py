"""
while és for ciklus között a különbség a for előre meghatározott mennyiségszer fog végrehajtódni
A while-t akkor használjuk amikor nem tudjuk milyen sokáig akarunk loopolni

a while után egy boolean képletnek kell jönnie
"""

# ez egy infinity loop amúgy
"""
while True:
    print("Hello")

"""


szam = 0

while szam < 10:
    print(f"Hello {szam}")
    szam += 2

#ez végre sem hajtóna mert False-al kezdődik
while False:
    print("Hello")
    szam += 1
