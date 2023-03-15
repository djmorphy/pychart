def hello():
    print(f"Hello! {__name__} modulból")   #ha direkbe futtatom akkor __main__ -t ír nem __name___-t
szam = 10
"""
ha if__name__ -be teszem akkor nem hajtóduk végre a 39-es modulban. Mert import után egyből kiprinteli a hello és számot
a 39-es 
__name__ az egy globális változó. minden file-al létrejön

ezt a __name__ == "__main_"" -t többnyire a file aljára teszem
"""


if __name__ == "__main__":
    hello()
    print(szam)

