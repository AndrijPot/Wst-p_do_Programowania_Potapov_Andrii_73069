def liczba(x):
    if x > 0:
        print("Liczba jest dodatnia")
    elif x == 0:
        print("Liczba jest równa zero")
    else:
        print("Liczba jest ujemna")

x = float(input("Znaczenie x: "))
liczba(x)

