import numpy as np

# Tworzymy macierz 5x5 wypełnioną zerami
macierz = np.zeros((5,5), dtype=int)

# Ustawiamy jedynki na krawędziach
macierz[0, :] = 1  # góra
macierz[-1, :] = 1 # dół
macierz[:, 0] = 1  # lewa
macierz[:, -1] = 1 # prawa

print("Macierz z krawędziami jedynek:")
print(macierz)

# Funkcja zamieniająca zera na jedynki i odwrotnie
def odwroc_macierz(mat):
    return 1 - mat

# Test funkcji
macierz_odwrocona = odwroc_macierz(macierz)
print("\nMacierz po odwroceniu 0 ↔ 1:")
print(macierz_odwrocona)