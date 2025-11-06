x = float(input("Podaj wartość x: "))

#a(x)
if x > 0:
    a = x*2
elif x == 0:
    a = 0
else:
    a = x * (-3)
#b(x)
if x >= 1:
    b = x**2
elif x < 1:
    b = x

#c(x)
if x > 2:
    c = x+2
elif x == 2:
    c = 8
elif x < 2:
    c = x - 4

print("a(x) =", a)
print("b(x) =", b)
print("c(x) =", c)
