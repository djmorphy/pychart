#varriable scope- valtozok láthatósága és élettartalma (lokális,globális)

"""
function scope, module, class scope
19_scope.py egy module-nak számít. Ennek van egy module scope-ja
Amit ebbe létrehozunk változót az globális változónak számít a module-on belül
a for és while-nak nincs saját scope-ja
"""
#ez a module scope. ezen a fileon belül bárhol elérhető
a = 78
b = 47

#ez a function scope-hoz tartozik. Élettartalma pedig létrehozza az "a" -t "b"-t kiírja és utána törli a memóriából
def test():

    global a #ezzel tudom a 78-at felülírni. A compailernek azt mondom hogy ne hozz létre külön még egy "a"-t hanem a meglévőt írd felül
    #global a,b  #vesszővel elválasztva
    a = 12
    b = 15
    print(a,b)

test()
print(a,b)


""" 
python nem úgy van mint JAVA-ban. ha létrehozom az i változót és lefut a for ciklus akkor nem törlődik a memoriából az i hanem
még mindig elérhető mert átfolyik a globalis változókba. A b JAVA-ban localis lenne de itt globalis
"""
for i in range(5):
    b = 55
    pass

print(i)
print(b)


#ezt a szivást a legjobban úgy oldhatom meg hogy egy berakom egy fgv()-be

def test2():
    for j in range(5):
        c=54
        pass

#print(j) #j így már nemlétezik

#ennek sincs  saját scopja
if True:
    q = 78

print(q)
#megoldása
def test3():
    if True:
        p = 78
#így hibát köp
#print(p)