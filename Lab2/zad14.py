import math
print("Wersja z CONTINUE")
while True:
    try:
        wejscie = input("Podaj liczbę całkowitą (nieujemną): ")
        dana = int(wejscie)
        if dana >= 0:
            pierwiastek = math.sqrt(dana)
            print(f"Pierwiastek: {round(pierwiastek, 2)}")
            continue

        break

    except ValueError:

        break

print("Dziękujemy za skorzystanie z naszej aplikacji")
print("\n\n\n\n")


print("--- Wersja BEZ continue ---")

while True:
    try:
        wejscie = input("Podaj liczbę całkowitą (nieujemną): ")
        dana = int(wejscie)

        if dana >= 0:
            print("To jest liczba dodatnia")
            pierwiastek = math.sqrt(dana)
            print(f"Pierwiastek: {round(pierwiastek, 2)}")
        else:
            break

    except ValueError:
        break

print("Dziękujemy za skorzystanie z naszej aplikacji")