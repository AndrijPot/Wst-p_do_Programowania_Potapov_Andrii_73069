def plec(imie):
    if imie.endswith('a'):
        return "kobieta"
    else:
        return "mężczyzna"

lista_imion = ["Anna", "Tomasz", "Julia", "Andrzej", "Ivan"]
slownik_plec = {}
for i in lista_imion:
    slownik_plec[i] = plec(i)
print(slownik_plec)