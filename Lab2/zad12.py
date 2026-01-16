print("Kalkulator średniej punktów grupy")

suma_punktow = 0
while True:
    try:
        n = int(input("Podaj liczbę studentów w grupie (n): "))
        if n > 0:
            break
        else:
            print("Liczba studentów musi być większa od 0!")
    except ValueError:
        print("Wpisz liczbę całkowitą.")

for i in range(1, n+1):

    while True:
        try:

            punkty = float(input(f"Podaj punkty dla studenta nr {i}: "))

            if punkty < 0:
                print('nie może być ujemne')
                continue
            else:
                suma_punktow += punkty
                break
        except ValueError:
            print("Wpisz liczbę całkowitą.")
            continue

srednia = suma_punktow / n
print(f"Średnia punktów w grupie: {round(srednia, 2)}")