import datetime

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))

data = datetime.datetime(rok, miesiac, dzien)

# a і b
print(f"Dzień roku: {data.strftime('%j')}")
print(f"Numer tygodnia: {data.strftime('%W')}")

# c
dwa_tygodnie = datetime.timedelta(weeks=2)
print(f"2 tyg. wcześniej: {data - dwa_tygodnie}")
print(f"2 tyg. później:   {data + dwa_tygodnie}")

# d
dni_do_niedzieli = (6 - data.weekday()) % 7
print(f"Najbliższa niedziela: {data + datetime.timedelta(days=dni_do_niedzieli)}")

# e
print(f"Czas Unix: {data.timestamp()}")