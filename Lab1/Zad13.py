a = float(input("Podaj wartość A: "))
b = float(input("Podaj wartość B: "))
działanie = input("Podaj działanie(+-*/): ")
match działanie:
    case "+":
        print(a+b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        # sprawdzamy, czy nie ma dzielenia przez 0
        if b != 0:
            print(a / b)
        else:
            print("Nie można dzielić przez zero!")

