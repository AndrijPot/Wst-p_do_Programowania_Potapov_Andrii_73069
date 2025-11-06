wiek = int(input("Ile masz lat? "))

if wiek >= 18 and wiek < 120:
    print("Jesteś pełnoletni")
elif wiek < 18 and wiek > 0:
    print("Jesteś nie pełnoletni")
else:
    print("Nieprawidłowy wiek")
