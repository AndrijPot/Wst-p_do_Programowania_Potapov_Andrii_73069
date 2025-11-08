zdanie=input("wpisz zdanie: ")
print(zdanie)

# A ver z tab alfabetu
alfabet = ["a", "b", "c", "d", "e", "f", "m"]
lb_w = [0,0,0,0,0,0,0]

for znak in zdanie:
    print("sprawdzam znak: ", znak)
    for i in range(len(alfabet)):
        print("czy jest to litera: ", alfabet[i])
        if znak == alfabet[i]:
            lb_w[i]+=1
            print("tak")

# B

wynik = zdanie[::2]
print("Po usunięciu znaków o nieparzystych indeksach:", wynik)

# C

lista_slow = zdanie.split()
print(lista_slow)

for slowo in lista_slow:
    nowe = slowo[0].upper() + slowo[1:-1] + slowo[-1].upper()
    print(nowe)

# D


max_slowo = max(lista_slow, key=len)
max_dlugosc = max(len(slowo) for slowo in lista_slow)

print("najdłuższe słowo i jego długość: ",max_slowo, max_dlugosc)

# E


seen = set()
result = []

for ch in zdanie:
    if ch in seen:
        result.append("@")
    else:
        result.append(ch)
        seen.add(ch)

print("Wynik:", "".join(result))