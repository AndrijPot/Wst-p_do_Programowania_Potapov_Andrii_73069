def st (a,n):
    if n == 0:
        return 1
    else:
        return a * st (a, n-1)

a = float(input("Podaj a: "))
n = float(input("Podaj n: "))

print(st (a,n))