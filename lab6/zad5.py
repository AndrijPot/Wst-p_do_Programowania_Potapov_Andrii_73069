import pandas as pd

# 1️⃣ Tworzymy DataFrame z danymi studentów
df = pd.DataFrame({
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
})

# a) Studenci z oceną > 4
studenci_ocena_gt4 = df[df['Ocena'] > 4]

# b) Sortowanie według wieku
df_sort_wiek = df.sort_values(by='Wiek')

# c) Średni wiek w grupach ocen
sredni_wiek = df.groupby('Ocena')['Wiek'].mean()

# d) Protokół ocen z poprawy i połączenie
df_poprawa = pd.DataFrame({
    'Nr_albumu': [2, 5],
    'Nowa_ocena': [4.0, 3.5]
})
df_polaczone = pd.merge(df, df_poprawa, on='Nr_albumu', how='left')

# e) Zapis do CSV
df_polaczone.to_csv('studenci.csv', index=False)

# f) Wczytanie CSV i sprawdzenie
df_sprawdzenie = pd.read_csv('studenci.csv')
print("Wczytany CSV:")
print(df_sprawdzenie)

# g) Dodanie nowego studenta
nowy_student = pd.DataFrame({
    'Nr_albumu': [6],
    'Imię': ['Ewa'],
    'Nazwisko': ['Mazur'],
    'Ocena': [4.8],
    'Wiek': [22]
})
df = pd.concat([df, nowy_student], ignore_index=True)

# h) Unikalne wartości w kolumnie 'Ocena'
unikalne_oceny = df['Ocena'].unique()
print("Unikalne oceny:", unikalne_oceny)

# i) Ile studentów ma ocenę równą 5
liczba_piątek = (df['Ocena'] == 5.0).sum()
print("Liczba studentów z oceną 5:", liczba_piątek)