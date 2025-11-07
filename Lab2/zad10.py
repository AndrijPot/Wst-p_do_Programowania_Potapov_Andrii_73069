x = int(input("Podaj liczbę X: "))
y = int(input("Podaj liczbę Y: "))
if x>y:
    for i in range(y,x+1):
        print(i)
else:
    for i in range(x,y+1):
        print(i)