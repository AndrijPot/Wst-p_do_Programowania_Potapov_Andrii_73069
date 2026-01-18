def znajdz_max(*args):
    if not args:
        return None
    print(f"Przetwarzane liczby: {args}")
    maksimum = max(args)
    return maksimum

wynik = znajdz_max(10, 5, 99, 2, 45)
print(f"Największa liczba to: {wynik}")