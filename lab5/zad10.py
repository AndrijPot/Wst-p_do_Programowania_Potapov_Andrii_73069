import math
import random

liczby = random.sample(range(1,50), 10)
new_touple = []


tuple(liczby)

start = float(input("Podaj początek przedziału: "))
koniec = float(input("Podaj koniec przedziału: "))

for i in liczby:
    if i >= start and i <= koniec:
        new_touple.append(i)

new_touple.sort()

if len(new_touple) > 0:
    geom = math.prod(new_touple) ** (1 / len(new_touple))
    print("Wylosowana krotka: ", tuple(new_touple))
    geom = math.prod(new_touple) ** (1/len(new_touple))
    print("Średnia geometryczna:", geom)
else:
    print("Brak liczb w tym przedziale — nie można obliczyć średniej.")

