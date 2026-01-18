import sys
import random
print("Losowanie z tablicy")

wejscie = input("Podaj 5 cyfr rozdzielonych przecinkiem (np. 1,2,3,4,5): ")
lista_str = wejscie.split(',')
try:
    liczby = [int(x.strip()) for x in lista_str]
except ValueError:
    print("To nie są poprawne liczby!")
    sys.exit()

if len(liczby) != 5:
    print(f"Wymagane jest dokładnie 5 liczb")
    sys.exit()
zbior_liczb = set(liczby)
wylosowana = random.choice(list(zbior_liczb))

print(f"Wylosowany element: {wylosowana}")

if wylosowana == min(liczby):
    print("To jest NAJMNIEJSZA liczba!")
elif wylosowana == max(liczby):
    print("To jest NAJWIĘKSZA liczba!")
else:
    print("To jest liczba 'środkowa' (ani min, ani max).")