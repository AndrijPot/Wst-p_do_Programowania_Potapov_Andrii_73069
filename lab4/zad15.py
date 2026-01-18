def palindrome(slowo):
    slowo = slowo.lower()
    reverse = slowo[::-1]
    if slowo == reverse:
        return "Słowo jest palindromem"
    else:
        return "Słowo nie jest palindromem"



slowo = input("Podaj slowo: ")
print(palindrome(slowo))