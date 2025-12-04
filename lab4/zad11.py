def wr(slowo):
    first = slowo [0]
    last = slowo [-1]
    middle = slowo [1:-1]
    if len(slowo) == 1:
        return slowo
    elif len(slowo) == 2:
        return last + first
    else:
        return last + wr(middle) + first

slowo = input("Podaj slowo: ")
print(wr(slowo))