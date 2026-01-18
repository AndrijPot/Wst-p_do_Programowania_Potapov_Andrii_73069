import math

def pole_trojkata(a, b, kat_stopnie):
    if a <= 0 or b <= 0 or kat_stopnie <= 0 or kat_stopnie >= 180:
        print("Boki muszą być dodatnie, a kąt między 0 a 90")
        return

    kat_rad = math.radians(kat_stopnie)

    c_kwadrat = a**2 + b**2 - 2 * a * b * math.cos(kat_rad)

    if (a**2 + c_kwadrat < b**2) or (b**2 + c_kwadrat < a**2):
        print("Trójkąt istnieje, ale jest rozwartokątny (inny kąt > 90°)")
        return

    pole = 0.5 * a * b * math.sin(kat_rad)
    print(f"Pole trójkąta ostrokątnego wynosi: {round(pole, 2)}")


pole_trojkata(10, 10, 60)

pole_trojkata(2, 100, 10)