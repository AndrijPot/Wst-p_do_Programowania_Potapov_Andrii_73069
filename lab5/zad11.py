import random

def gra():
    while True:
        try:
            start = int(input("Podaj dolną granicę (od): "))
            end = int(input("Podaj górną granicę (do): "))
            if start >= end:
                print("❌ Błąd: Dolna granica musi być mniejsza od górnej! Popraw zakres.")
                continue
        except ValueError:
            print("Proszę podać liczbę całkowitą!")
            continue
        if (end - start) <= 2:
            print("Bardzo mały zakres")
            continue
        break

    wylosowana_liczba = random.randint(start, end)
    print("Masz dokładnie 3 próby.")
    próba = 1
    while próba <= 3:
        try:
            user_num = int(input(f"Próba {próba}: "))
        except ValueError:
            print("Proszę podać liczbę całkowitą!")
            continue

        if user_num == wylosowana_liczba:
            print(f"Zgadłeś liczbę {wylosowana_liczba}!")
            return
        elif user_num < wylosowana_liczba:
            print("Za mało!")
            próba += 1
        else:
            print("Za dużo!")
            próba += 1
    print(f"Przegrałeś. Wyczerpałeś limit prób")
    print(f"Szukana liczba to: {wylosowana_liczba}")
gra()