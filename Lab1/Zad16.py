import math
print("Obliczanie pola i obwodu trójkąta")
try:
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))
    if a + b > c and a + c > b and b + c > a:
        obwod = a + b + c
        p = obwod / 2
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))

        print(f"Wyniki dla boków {a}, {b}, {c}:")
        print(f"Obwód: {obwod}")
        print(f"Pole: {round(pole, 2)}")

    else:
        print("Z podanych boków NIE da się zbudować trójkąta.\nSuma dwóch krótszych boków musi być większa od najdłuższego.")

except ValueError:
    print("Proszę podać liczbę, a nie tekst")