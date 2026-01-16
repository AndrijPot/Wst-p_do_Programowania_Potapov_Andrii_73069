print("Zamiana wielkości liter")
while True:
    litera = input("Podaj jedną literę: ")
    if len(litera) == 1 and litera.isalpha():
        if litera.islower():
            litera = litera.upper()
            print(f"Teraz litera '{litera}' jest duża.")
            break
        else:
            litera = litera.lower()
            print(f"Teraz litera '{litera}' jest mała.")
            break
    else:
        print("Podaj tylko jedną literę")
        continue