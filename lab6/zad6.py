import pandas as pd
import matplotlib.pyplot as plt

# Dane przykładowe
dane = {
    'Kategoria': ['Elektronika', 'Odzież', 'Meble', 'Kosmetyki', 'Zabawki'],
    'Sprzedaz': [120, 80, 50, 70, 40]
}

# Tworzymy DataFrame
df = pd.DataFrame(dane)

# Tworzymy wykres słupkowy
plt.figure(figsize=(8,5))
plt.bar(df['Kategoria'], df['Sprzedaz'], color='skyblue')
plt.title('Ilość sprzedanych produktów w różnych kategoriach')
plt.xlabel('Kategoria')
plt.ylabel('Ilość sprzedanych produktów')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()