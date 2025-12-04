def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    n = fibonacci(n - 1) + fibonacci(n - 2)
    return n

n = int(input("Podaj n: "))
print(fibonacci(n))