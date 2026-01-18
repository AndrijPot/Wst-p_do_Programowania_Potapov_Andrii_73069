import random
print("Szybkie operacje na zbiorach")

X = set(random.sample(range(11), random.randint(3, 7)))
Y = set(random.sample(range(11), random.randint(3, 7)))

print(f"X: {X}")
print(f"Y: {Y}")

#a
print(f"a) Czy 5 jest w X? {5 in X}")
#b
print(f"b) Czy X to podzbiór Y? {X <= Y}")
#c
print(f"c) Czy Y to podzbiór X? {Y <= X}")
#d
print(f"d) Suma (X | Y): {X | Y}")
#f
print(f"f) Różnica (Y - X): {Y - X}")
#g
print(f"g) Iloczyn (X & Y): {X & Y}")
#h
print(f"h) Max z sumy: {max(X | Y)}")

#i
Y.add(X.pop())
print(f"i) Przeniesiono losowy element z X do Y.\nX: {X}\nY: {Y}")

# j
Y |= X
print(f"j) Skopiowano resztę elementów X do Y: {Y}")

# k) Czyszczenie
X.clear();
Y.clear()
print(f"k) Wyczyszczono zbiory: X={X}, Y={Y}")