import string
alfabet = list(string.ascii_lowercase)
try:
    n = int(input("Podaj n: "))
    if n > 0:
        wynik = []
        for i in range(0, len(alfabet), n):
            podlista = alfabet[i: i + n]
            wynik.append(podlista)

            # 4. Wyświetlenie wyniku

        print(wynik)
    else:
        print("N musi być większe od 0.")
except ValueError:
    print("Proszę podać liczbę całkowitą!")




