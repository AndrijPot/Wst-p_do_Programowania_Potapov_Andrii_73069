print("Sprawdzanie wielkości litery")
tekst = input("Podaj jedną literę: ")

if len(tekst) != 1:
    print("Musisz podać dokładnie jeden znak")
elif not tekst.isalpha():
    print("To nie jest litera")
elif tekst.isupper():
    print(f"Litera '{tekst}' jest duża.")
elif tekst.islower():
    print(f"Litera '{tekst}' jest mała.")