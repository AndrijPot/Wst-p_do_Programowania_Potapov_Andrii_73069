import pandas as pd

df = pd.read_csv(
    "demografia.csv",
    decimal='.',
    na_values='.'
)

df_lata = df.drop(columns='KRAJE')
max_przyrost = df_lata.max().max()
rok = df_lata.max().idxmax()
idx = df_lata[rok].idxmax()
kraj = df.loc[idx, 'KRAJE']

print("Największy przyrost ludności:", max_przyrost)
print("Rok:", rok)
print("Kraj:", kraj)