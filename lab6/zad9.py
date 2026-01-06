import pandas as pd
import matplotlib.pyplot as plt

# Przykładowe dane – oceny studentów
oceny = [2, 3, 3, 4, 4, 4, 5, 5, 3, 4, 2, 5, 4, 3, 5]

# DataFrame
df = pd.DataFrame({"Ocena": oceny})

# Histogram
plt.hist(df["Ocena"], bins=4)
plt.xlabel("Ocena")
plt.ylabel("Liczba studentów")
plt.title("Rozkład ocen studentów")
plt.grid(True)

plt.show()