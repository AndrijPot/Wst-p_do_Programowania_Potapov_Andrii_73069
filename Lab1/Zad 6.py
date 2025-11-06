# Zadanie 6
droga = float(input("Długość przejechanej drogi: "))
paliwo = float(input("Średnie zużycie paliwa na 100 km: "))

zużycie = droga * 0.01 * paliwo
koszty = zużycie * 6.5
print("przewidywane zużycie paliwa:", zużycie, "l")
print("przybliżone koszty podróży:", koszty, "zl")