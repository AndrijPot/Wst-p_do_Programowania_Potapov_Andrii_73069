import numpy as np

macierz = np.random.randint(0, 100, size=(5, 5))
print("Macierz 5x5:\n", macierz)

najwiekszy = np.max(macierz)
najmniejszy = np.min(macierz)
print("\nNajwiększy element:", najwiekszy)
print("Najmniejszy element:", najmniejszy)

max_wiersze = np.max(macierz, axis=1)
print("\nNajwiększe elementy w wierszach:", max_wiersze)

max_kolumny = np.max(macierz, axis=0)
print("Największe elementy w kolumnach:", max_kolumny)

suma_wiersze = np.sum(macierz, axis=1)
print("Suma wartości w wierszach:", suma_wiersze)