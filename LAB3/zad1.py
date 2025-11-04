imie = ["Andrii", "Adam", "Obama"]
print(imie)
for i in imie:
    print(i)

for i in range(len(imie)):
    print(f"index: {i}, imie: {imie[i]}")

# A ver 1
print((sorted(imie)))
# ver 2
posortowane_imie = sorted(imie)
print(posortowane_imie)

#B
imie.append("Kasia")
imie.append("Ala")
print(imie)
print(imie.pop())
print(imie)

#C
imie.insert(3, "Basia")
print(imie)

#D
imie.reverse()
print(imie * 2)