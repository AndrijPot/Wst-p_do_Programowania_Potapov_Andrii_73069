def bmi(x, y):
    wynik = x/((y)**2)
    if wynik < 17:
        print("Znaczna niedowaga")
    elif wynik >= 17 and wynik < 18.5:
        print("Niedowaga")
    elif wynik >= 18.5 and wynik < 25:
        print("Normalna waga")
    elif wynik >= 25 and wynik < 30:
        print("Nadwaga")
    elif wynik >= 30 and wynik < 35:
        print("Otyłość I stopnia")
    elif wynik >= 35 and wynik < 40:
        print("Otyłość II stopnia")
    elif wynik >= 40:
        print("Otyłość III stopnia")
    else:
        print("nieprawidłowe liczby")
    return wynik
waga = float(input("Waga: "))
wzrost = float(input("Wzrost m: "))


print(f"Twoj BMI: {round(bmi(waga, wzrost), 2)}")