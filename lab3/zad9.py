print("Mapa Gry")
print("Legenda: . trawa, x przeciwnik, * moneta, = rzeka\n")
szerokosc = 6
wysokosc = 5


przeciwnicy = [(0,1), (2,3), (2,4), (3,4)]
monety = [(1,1), (2,0), (3,3), (5,3)]

for y in range(wysokosc):
    for x in range(szerokosc):
        obecny_punkt = (x, y)

        if obecny_punkt in przeciwnicy:
            print("X", end=" ")
        elif obecny_punkt in monety:
            print("*", end=" ")
        elif y == 2:
            print("=", end=" ")
        else:
            print(".", end=" ")
    print()