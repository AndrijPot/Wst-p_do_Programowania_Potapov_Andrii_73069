from datetime import datetime

ostatnie_laboratoria_str = input("Podaj datę ostatnich laboratoriów (YYYY-MM-DD): ")
kolokwium_str = input("Podaj datę kolokwium (YYYY-MM-DD): ")

ostatnie_laboratoria = datetime.strptime(ostatnie_laboratoria_str, "%Y-%m-%d")
kolokwium = datetime.strptime(kolokwium_str, "%Y-%m-%d")

dzisiaj = datetime.today()

dni_od_laboratoriow = dzisiaj - ostatnie_laboratoria
dni_do_kolokwium = kolokwium - dzisiaj

print(f"Ostatnie laboratoria były: {ostatnie_laboratoria.day} {ostatnie_laboratoria.strftime('%B')} {ostatnie_laboratoria.year}")
print(f"Dni, które minęły od ostatnich laboratoriów: {dni_od_laboratoriow}")
print(f"Kolokwium odbędzie się: {kolokwium.day} {kolokwium.strftime('%B')} {kolokwium.year}")
print(f"Dni pozostałe do kolokwium: {dni_do_kolokwium}")