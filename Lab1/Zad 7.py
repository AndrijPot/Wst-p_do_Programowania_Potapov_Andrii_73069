import random
from random import randint
droga = randint(1, 1000)

paliwo = float(input("Średnie zużycie paliwa na 100 km: "))

zużycie = droga * 0.01 * paliwo
koszty = zużycie * 6.5
print("Długość przejechanej drogi:", droga)
print("przewidywane zużycie paliwa:", zużycie, "l")
print("przybliżone koszty podróży:", koszty, "zl")
