import numpy as np

macierz = np.random.randint(0, 51, size=(5, 5))
print("Macierz 5x5:\n", macierz)

elementy_wieksze_20 = macierz[macierz > 20]
print("\nElementy większe niż 20:", elementy_wieksze_20)

liczba_elementow = elementy_wieksze_20.size
print("Liczba elementów większych niż 20:", liczba_elementow)

srednia = np.mean(macierz)
print("Średnia wartość w macierzy:", srednia)