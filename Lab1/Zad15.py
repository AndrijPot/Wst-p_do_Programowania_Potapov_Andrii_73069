print("Mamy równanie liniowe 0 = ax + b")
while True:
    try:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        break
    except ValueError:
        print("Proszę podać liczbę, a nie tekst")
        continue

# Sprawdzamy, czy nie dzielimy przez zero
if a == 0 and b == 0:
    print("Nieskończenie wiele rozwiązań (0 = 0)")

elif a == 0:
    print("Brak rozwiązań")
else:
    x = -(b / a)

    print(f"X: {round(x, 2)}")