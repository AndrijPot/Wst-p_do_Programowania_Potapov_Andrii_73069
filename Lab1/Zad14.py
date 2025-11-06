# Pobieramy nazwę pliku od użytkownika
nazwa_pliku = input("Podaj nazwę pliku: ")

# Sprawdzamy czy plik jest arkuszem Excel
if nazwa_pliku.endswith(".xls") or nazwa_pliku.endswith(".xlsx"):
    print("To jest plik arkusza Excel.")
else:
    print("To nie jest plik Excel.")