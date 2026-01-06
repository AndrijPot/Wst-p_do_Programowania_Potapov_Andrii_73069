import numpy as np

lista = [128, 64, 32, 16, 8, 4, 2, 1]

wagi = np.array(lista)

liczba_bin = np.random.randint(0, 2, size=8)

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

print("Wagi:        ", wagi)
print("Liczba bin:  ", liczba_bin)
print("Wartość dec: ", wartosc_liczby_bin(wagi, liczba_bin))
