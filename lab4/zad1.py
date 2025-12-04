import math
def pole (rad):
    S = math.pi * rad**2
    return S

r = input("Znaczenie R: ")
print("Pole koła wynosi:", pole(float(r)))