# modules, namespace and importing - modulok, nevterek és importálás

# full math.py importálja
#import math

#ha csak a sin és cos fgv kell
#from math import sin, cos

#print(math.pi)
#print(math.sqrt(8))

#print(math.sin(4))
#print(math.cos(4))

import MyModule
#import Tester.MyModule

#beka aliasként hívom meg és így hivatkozok rá
import Tester.MyModule as beka

MyModule.hello()
print(MyModule.szin)
print(MyModule.nevek)

#mivel egy beka alai-st letrehoztam így ez csak beka-ként működik. Ha nincs alias
#akkro ez működne
#Tester.MyModule.hello()

beka.hello()

#a MyModule-ból csak az osztályt importálom be //ha nincs a felette lévő sorok amiket írtam

from MyModule import Osztaly

#objektum létrehozása
o = Osztaly()


""" azért nem jó mert akkor a hello()-t ugyan végre hajtja de jelzi hogy itt is van hello és a mymodule-ban is
ezért jobb ha import Mymodile és kész
"""

# from Mymodule import hello
def hello():
    print("Hello a fő modulból")

hello()

