import pandas as pd

# Utworzenie DataFrame
df = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
})

# a) Pensja > 5000
pracownicy_5000 = df[df['Pensja'] > 5000]

# b) Sortowanie według wieku
df_sort_wiek = df.sort_values(by='Wiek')

# c) Średnia pensja według stanowiska
srednia_pensja = df.groupby('Stanowisko')['Pensja'].mean()

# d) Zmiana stanowiska i połączenie
df_awans = pd.DataFrame({
    'ID': [2, 4],
    'Nowe_stanowisko': ['Senior Programista', 'Senior Programista']
})
df_polaczone = pd.merge(df, df_awans, on='ID', how='left')

# e) Zapis do CSV
df_polaczone.to_csv('pracownicy.csv', index=False)

# f) Wczytanie z CSV
df_sprawdzenie = pd.read_csv('pracownicy.csv')

print(df_sprawdzenie)
