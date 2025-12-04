def pole(a, b, c):
    # Sprawdzenie poprawności długości trójkąta, dla którego można obliczyć pole powierzchni
    while True:
        if a<b+c:
            break
        else:
            print("Bok A trójkąta jest nieprawidłowy")
            a = float(input("Podaj strone a: "))
            continue
    while True:
        if b<a+c:
            break
        else:
            print("Bok B trójkąta jest nieprawidłowy")
            b = float(input("Podaj strone b: "))
            continue
    while True:
        if c<a+b:
            break
        else:
            print("Bok C trójkąta jest nieprawidłowy")
            c = float(input("Podaj strone c: "))
            continue

    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    return S

a = float(input("Podaj strone a: "))
b = float(input("Podaj strone b: "))
c = float(input("Podaj strone c: "))

print("Pole: ", round(pole(a, b, c), 2))
