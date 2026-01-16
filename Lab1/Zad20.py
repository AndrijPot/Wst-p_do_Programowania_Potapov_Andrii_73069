print("Kalkulator Wyniku Drużyny")
bonus = 0
while True:
    try:
        gol = int(input("Podaj liczbę strzelonych bramek: "))
    except ValueError:
        print("Proszę podać liczbę całkowitą!")
        continue
    if gol < 0:
        print("Gole nie mogą być ujemne")
        continue
    else:
        break
laczny_wynik = gol * 10


if gol >= 5:
    laczny_wynik += 5

if gol >= 10:
    laczny_wynik += 10

print(f"Łączny wynik drużyny: {laczny_wynik}")
