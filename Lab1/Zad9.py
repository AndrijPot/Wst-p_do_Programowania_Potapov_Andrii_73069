wiek = int(input("Ile masz lat? "))

if wiek > 0 and wiek <= 4:
    print("Cennik biletowy: 0 zl")
elif wiek > 4 and wiek < 18:
    print("Cennik biletowy: 10 zl")
elif wiek >= 18 and wiek < 100:
    student = input("Jesteś studentem?(tak/nie) ")
    if student == "tak":
        print(f"Cennik biletowy: {20*0.75} zl")
    elif student == "nie":
        print("Cennik biletowy: 20 zl")
else:
    print("Nieprawidłowy wiek")
