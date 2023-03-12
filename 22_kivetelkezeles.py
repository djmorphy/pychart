#eception handing (error handing) - kivétel kezelés
"""
Ha egy vagy több hiba keletkezhet de nem akarjuk hogy leáljon a program
"""

lista = [1,2,3]


try:
    #print(bla)
    #print(lista[4])
    print(1 / 0)
except NameError as e:  #az "e" az csak egy konvenció hogy error
    print(e,'- Nem létező változó')
except IndexError as e:
    print(e, '- Tartományom kívüli index')
except ZeroDivisionError as e:
    print(e,'- hülye! nullával való osztásnak mi értelme?')
print(" a program vége exception1")

lista2 = ['1', '2', '3', None, '4','','5', True, 'Bözsi', '12.64']
for i in lista2:
    try:
        print(int(i)*2)
    except:
        continue
print("a program vége exception2")

print()
"""
struktúra

try:
    print('bla')
except:
    pass
else:
    pass
finally:
    pass

except-ből bármennyi lehet
else-ből egy lehet
finally-ből is egy lehet

Próbáld meg a try blokkot végrehajtani.
ha nem tudod végre hajtani akkor hajdtsd végre az except blokkot
és miután végrehajtott az except blockot hajtsd végre a finally blockot

Ha végre tudtad a try blockot hajtani akkor hajtsd végre ami az else-ben van
és végül hajtsd végre a finaly-ben

Ha a try le tud futni akkor lefut az else és a finally is
"""


try:
    print(bla)
except:
    print('nem, jó változó név')
else:
    print('az else!')
finally:
    print('try vége')


print()
print()
try:
    print('bla')
except:
    print('nem, jó változó név')
else:
    print('az else!')
finally:
    print('try vége')