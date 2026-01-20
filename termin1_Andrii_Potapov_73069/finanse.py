from wydatki import pln_na_usd, procent_z_kwoty, suma_wydakow

# 1)
pln = 500
print(f"Z {pln} PLN to {pln_na_usd(pln)} USD")

# 2)
proc = 15
wydatki = 1200
print(f"{proc}% z {wydatki} PLN to {procent_z_kwoty(proc,wydatki)} PLN")

# 3)
lista_wydatków = [200,300,400]
print(f"Suma wydatków z listy {lista_wydatków} to {suma_wydakow(lista_wydatków)}")

#B
wydatki_marzec = [1200, 500, 700]
wydatki_kwiecień = [900, 800,500]
wydatki_maj = [400, 600, 300]

# Suma dla trzech kolejnych miesięcy
sumy_miesieczne = sum([suma_wydakow(wydatki_marzec), suma_wydakow(wydatki_kwiecień), suma_wydakow(wydatki_maj) ])

print(f"Suma wydatków w marcu: {suma_wydakow(wydatki_marzec)}")
print(f"Suma wydatków w kwietniu: {suma_wydakow(wydatki_kwiecień)}")
print(f"Suma wydatków w maju: {suma_wydakow(wydatki_maj)}")

# Liczymy średnie:
średnie = sumy_miesieczne/3

print(f"Średnia kwota wydatków miesięcznych: {round(średnie, 2)}")