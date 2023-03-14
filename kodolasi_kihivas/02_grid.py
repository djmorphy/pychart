"""
Írj egy függvényt, ami egy 2 dimenziós rácsos szerkezetet hoz létre (grid).
A függvénynek két bemeneti paramétere legyen: row, column (sor, oszlop)
Töltsd ki ezt a rácsot csupa nullával.
Pseudo kód:
függvény definíció(row, column)
    rács lista []
    külső ciklus y (row)
        rács listához hozzádunk egy belső üres listát
        belső ciklus x (column)
            a rács lista belső listájába (rács lista az y indexnél), hozzáadunk egy nullát

    végül visszadjuk a rács listát
g = grid_create(5, 5)
print(g)
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Majd definiálj még egy függvényt, ami egy rács bementet fogad, és kiírja ezt a rácsot a konzolra, sorról sorra.
grid_print(g)
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
Az első függvény neve legyen: grid_create
A második függvény neve legyen: grid_print

"""
#2D rács létrehozása
def grid_create(row, col):
    grid = []
    for y in range(row):
        #valahányszor lefut a külső ciklus a grid listába bele appendelok egy üres listát
        grid.append([])
        #belső loopot hozok létre
        for x in range (col):
            #az y indexnél add hozzá a nullát
            grid[y].append(0)
    return grid


#a rács összes sorát egyesével kiprinteli
def grid_print(grid):
    for row in grid:
        print(row)



g = grid_create(4, 5)
grid_print(g)