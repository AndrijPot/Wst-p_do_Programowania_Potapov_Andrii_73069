zdanie=input("wpisz zdanie: ")

lista_slow = zdanie.split(" ")
for slowo in lista_slow:
    if slowo[0::] == slowo[::-1]:
        print(f"Slowo '{slowo}' jest onimem")
    else:
        print(f"Slowo '{slowo}' nie jest onimem")
