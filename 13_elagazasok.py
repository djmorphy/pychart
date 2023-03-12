#if statements, conditionals - elágazások, kondicionálisok
"""
az if után egy boolean képlet jön
"""


if True:
    print('igaz')

#ez nem írodik ki
if False:
    print('hamis')



eletkor = 20
#nem fut le
if eletkor < 18:
    print("Se cigi se pia de kávé igen")

eletkor = 17

if eletkor < 18:
    #nested
    if eletkor >= 16:
        print('Egy kis sört megihatsz')
    else:
        print('Se cigi se pia csak kávé')

elif eletkor >= 18 and eletkor < 30:
    print('Jó bulizást')
elif eletkor > 30 and eletkor <65:
    print('Munka és család')
else:
    print("Nyugdíjas élet, meg unokák")