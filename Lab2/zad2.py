# zadanie 2 A
lb_a = int(input("Podaj liczbe wierszy "))
for i in range (lb_a):
    print("***")

# zadanie 2 B
lb_b = int(input("Podaj liczbe wierszy "))
liczba_gwiazd = 0
for i in range (lb_b):
    liczba_gwiazd += 1
    print("*" * liczba_gwiazd)

# zadanie 2 C
lb_c = int(input("Podaj liczbe wierszy "))
star = ""
space = " "
for i in range (lb_c):
    star += "* "
    print(lb_c*space, star)
    lb_c += -1





