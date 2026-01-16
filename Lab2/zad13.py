print("Kalkulator średniej (zabezpieczenie 0-100 pkt)")

while True:
    try:
        n = int(input("Podaj liczbę studentów w grupie (n): "))
        if n > 0:
            break
        print("Liczba studentów musi być większa od 0!")
    except ValueError:
        print("Wpisz liczbę całkowitą.")

licznik = 0
suma_punktow = 0

while True:
    if licznik == n:
        break

    try:
        punkty = float(input(f"Podaj punkty dla studenta nr {licznik + 1}: "))

        if punkty < 0 or punkty > 100:
            print("Punkty muszą być z przedziału 0 - 100!")
            continue

        suma_punktow += punkty
        licznik += 1

    except ValueError:
        print("To nie jest liczba.")
        continue

srednia = suma_punktow / n
print(f"Średnia punktów w grupie: {round(srednia, 2)}")