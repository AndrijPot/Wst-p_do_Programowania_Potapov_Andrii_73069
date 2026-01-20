
budżet = {
    "jedzenie": [140, 150, 170],
    "rozrywka": [50, 25, 70],
    "siłownia": [50, 60, 60]
}

system = True

while system:
    user_wybór = input("Co chcesz zrobić (dodać, suma, usuń, max, limit, exit)? ").lower()

    if user_wybór == "dodać":
        users_kategoria = input("Dodaj nową kategorię: ")
        lista_wydatków = []

        while True:
            users_wydatki = input("Zapisz wszystkie wydatki (jeśli to wszystko, '-'): ")

            if users_wydatki == "-":
                break

            try:
                users_wydatki_int = int(users_wydatki)
                lista_wydatków.append(users_wydatki_int)
            except ValueError:
                print("Tylko liczby!")
                continue

        if len(lista_wydatków) != 0:
            budżet[users_kategoria] = lista_wydatków
            print(f"Dodano kategorię '{users_kategoria}'")
        else:
            print("Nie dodano kategorii — brak wydatków.")


    # wyświetlenie sumarycznych wydatków
    elif user_wybór == "suma":
        for keys, values in budżet.items():
            print(f"{keys} : {sum(values)}")

    # usuń kategorię
    elif user_wybór == "usuń":
        print(budżet)
        users_kategoria = input("Którą kategorię chcesz usunąć?: ")

        # sprawdźmy, czy kategoria znajduje się na liście
        if users_kategoria in budżet.keys():
            budżet.pop(users_kategoria)
            print(f"Kategoria {users_kategoria} została usunięta")
        else:
            print("Nie ma takiej kategorii!")

    # najwyższy wydatek
    elif user_wybór == "max":
        max_kategoria = None
        max_suma = 0

        for kategoria, wydatki in budżet.items():
            suma = sum(wydatki)

            if suma > max_suma:
                max_suma = suma
                max_kategoria = kategoria

        print(f"\nNajwiększa suma wydatków: {max_kategoria} : {max_suma} ")


    #liczymy średnie znaczenia
    elif user_wybór == "średnie":
        for kategoria, wydatki in budżet.items():
            suma = sum(wydatki)
            print(f"{kategoria}: {round(suma/len(wydatki), 2)}")


    elif user_wybór == "limit":
        try:
            users_limit = int(input("Napisz limit: "))
        except ValueError:
            print("Tylko liczby!")
            continue
        znaleziono = False
        for kategoria, wydatki in budżet.items():
            suma = sum(wydatki)
            if suma > users_limit:
                print(f"{kategoria} : {suma}")
                znaleziono = True

        if not znaleziono:
            print("Nie ma kategorii przekraczającej limit")

    # dla wyjścia
    elif user_wybór == "exit":
        system = False

    else:
        print("Nie ma takiej funkcji!")


