import numpy as np

tablica = np.zeros((3, 3), dtype=int)
print("Początkowa tablica:\n", tablica)

tablica[0, 0] = 1
tablica[1, 1] = 1
tablica[2, 2] = 1

print("\nTablica po wypełnieniu:\n", tablica)