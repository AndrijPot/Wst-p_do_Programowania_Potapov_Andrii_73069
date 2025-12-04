import random
# A
print(f"szczęśliwy numerek: {random.randint(1,10)}")

# B
rok = [2000,2001,2002,2003,2004,2005,2006,2007,2008]
print(f"szczęśliwy rocznik: {random.choice(rok)}")

#C

liczby = list(range(1,50))
wylosowane = random.sample(liczby, 6)
print("Wylosowane liczby to:", wylosowane)