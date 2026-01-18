def znajdz_wspolne(a, b):
    zbior1 = set(a)
    zbior2 = set(b)

    wspolne = zbior1 & zbior2

    return list(wspolne)

lista_a = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
print(f"Lista A: {lista_a}")
lista_b = [-1, 4, 5, 6, 7, 8]
print(f"Lista B: {lista_b}")


wynik = znajdz_wspolne(lista_a, lista_b)


print(f"Wspólne elementy: {wynik}")