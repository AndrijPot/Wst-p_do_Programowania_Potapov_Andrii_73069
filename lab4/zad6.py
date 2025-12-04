def przedstaw_wiek(imie, wiek=20):
    """
    Funkcja przyjmuje imię i wiek osoby (domyślnie 20 lat),
    a następnie wyświetla informacje o tej osobie.

    Parametry:
    imie (str) – imię osoby
    wiek (int, opcjonalnie) – wiek osoby, domyślnie 20
    """
    print(f"{imie} ma {wiek} lat.")


# Wyświetlenie opisu funkcji
print("Opis funkcji:")
print(przedstaw_wiek.__doc__)
print()

# Wywołanie z podaniem wieku
przedstaw_wiek("Anna", 25)

# Wywołanie bez podania wieku – użyje wartości domyślnej
przedstaw_wiek("Marek")