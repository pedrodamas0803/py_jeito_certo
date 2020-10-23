
# |L1 -L2| < L3 < L1 + L2
def verifica_lado(a, b, c):
    if abs(b - c) < a and a < b + c:
        return True
    else:
        return False

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if verifica_lado(a, b, c) and verifica_lado(b, a, c) and verifica_lado(c, a, b):
    
    p = (a + b + c)/2

    area = (p * (p - a) * (p - b) * (p - c))**(0.5)
    print('Area é:', area)
else:
    print('Triangulo impossivel')