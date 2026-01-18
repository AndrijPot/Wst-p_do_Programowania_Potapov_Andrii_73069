def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

while True:
    try:
        a = int(input("podaj a: "))
        b = int(input("podaj b: "))
        break
    except ValueError:
        print("Proszę podać liczbę całkowitą!")
        continue

print(f"Wynik: {nwd(a, b)}")
