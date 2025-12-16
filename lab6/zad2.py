import pandas as pd

df = pd.read_csv(
    "demografia.csv",
    decimal='.',
    na_values='.'
)

# Znalezienie indeksu kraju z największym przyrostem ludności w 2022 roku
idx = df['2022'].idxmax(skipna=True)

# Pobranie nazwy kraju
kraj = df.loc[idx, 'KRAJE']

print("Kraj z największym przyrostem ludności w 2022:", kraj)