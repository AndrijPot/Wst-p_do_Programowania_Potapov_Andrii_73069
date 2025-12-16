import pandas as pd
import matplotlib.pyplot as plt

dane = {
    "CZAS": [0,1,2,3,4,5],
    "PREDKOSC": [0, 10, 27, 40, 45, 50]
}

df = pd.DataFrame(dane)
df.plot(
    x='CZAS',
    y='PREDKOSC',
    kind='scatter',
    title="Zaleznosc predkosci chwilowej od czasu",
    xlabel='Czas w sekundach',
    ylabel='Predkosc chwilowa pojazdu'

)

plt.grid(True)
plt.show()