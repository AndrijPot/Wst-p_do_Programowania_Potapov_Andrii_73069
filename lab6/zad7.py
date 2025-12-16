import pandas as pd
import matplotlib.pyplot as plt

# Dane przykładowe
dane = {
    'Kategoria': ['Elektronika', 'Odzież', 'Meble', 'Kosmetyki', 'Zabawki'],
    'Sprzedaz': [120, 80, 50, 70, 40]
}

# Tworzymy DataFrame
df = pd.DataFrame(dane)

# Tworzymy wykres kołowy
plt.figure(figsize=(7,7))
plt.pie(
    df['Sprzedaz'],
    labels=df['Kategoria'],
    autopct='%1.1f%%',  # procenty na wykresie
    startangle=90,      # początkowy kąt
    colors=['skyblue', 'lightgreen', 'salmon', 'gold', 'violet']
)
plt.title('Procentowy udział kategorii w całkowitej sprzedaży')
plt.show()
