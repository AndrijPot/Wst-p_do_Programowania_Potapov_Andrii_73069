while True:            # pętla nieskończona
    liczba = int(input("Podaj liczbę: "))
    if liczba < 0:     # jeśli liczba ujemna → wyjście z pętli
        break
    print("Podałeś:", liczba)