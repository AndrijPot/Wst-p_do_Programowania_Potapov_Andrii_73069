# # a
# imie = input("Podaj imię: ")
# print("Witaj", imie)
#
# # b
# wiek = int(input("Podaj swój wiek: "))
# print("Twój wiek to:", wiek)
#
# # c
# imie = input("Podaj imie: ")
# nazwisko = input("Podaj nazwisko: ")
# print(f"inicjały: {imie[0].capitalize()}.{nazwisko[0].capitalize()}.")
#
# # d
# tekst = input("Podaj tekst: ")
#
# for i in range(5):
#     print(tekst)
#
# # e
# tekst1 = input("Podaj pierwszy tekst: ")
# tekst2 = input("Podaj drugi tekst: ")
#
# tekst3 = tekst1 + tekst2
#
# print("Połączony łańcuch:", tekst3)

#f
tekst1_f = input("Podaj pierwszy tekst: ")
tekst2_f = input("Podaj drugi tekst: ")

polowa1 = len(tekst1_f) // 2
polowa2 = len(tekst2_f) // 2

tekst3_f = tekst1_f[:polowa1] + tekst2_f[polowa2:]

print("Wynik:", tekst3_f)