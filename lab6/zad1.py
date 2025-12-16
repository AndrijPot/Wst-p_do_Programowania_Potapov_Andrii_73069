import pandas as pd

# Wczytanie pliku CSV
df = pd.read_csv(
    "demografia.csv",
    decimal=',',
    na_values=['NA', 'n/a', 'NaN']
)

# Wyświetlenie danych
print(df)