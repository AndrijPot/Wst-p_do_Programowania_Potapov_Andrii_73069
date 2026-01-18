def czy_anagram(slowo1, slowo2):
    s1 = slowo1.lower().replace(" ", "")
    s2 = slowo2.lower().replace(" ", "")

    return sorted(s1) == sorted(s2)


w1 = input("Podaj pierwsze słowo (lub '-'): ")

w2 = input("Podaj drugie słowo: ")
if czy_anagram(w1, w2):
    print(f"'{w1}' i '{w2}' to anagramy.")
else:
    print(f"To nie są anagramy.")