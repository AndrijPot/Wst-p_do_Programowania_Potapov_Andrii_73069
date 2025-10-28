wiek = int (input("Ile masz lat: "))

if wiek >= 18:
    stud = input("Jestes studentem?(tak/nie): ")
    if stud.lower() == "tak":
        stud = True
    elif stud.lower() == "nie":
        stud = False

if wiek < 4 and wiek > 0:
    print("Cena biletowy: 0")
elif wiek >=4 and wiek < 18:
    print("Cena biletowy: 10", )
elif wiek >= 18 and stud == True:
    print("Cena biletowy: ", 0.75 * 20)
elif wiek >= 18:
    print("Cena biletowy: 20 ")


