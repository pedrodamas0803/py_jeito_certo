# Um programa que recebe um numero inteiro do usuario e responde se é par
import math 


def ehPar(numero):
    """Determina se um numero é par """
    if numero % 2 == 0:
        return True
    else:
        return False

def maximo(lista):
    maior = -1E9
    for n in lista:
        if n > maior:
            maior = n
    return maior

def media(lista):
    m = 0
    for n in lista:
        m = m + n
    return m/len(lista)

def fatorial(n):
    produto = 1
    while n > 0:
        produto = produto * n
        n = n - 1
    return produto

def buscar(lista, elemento):
    indice = None
    for i in range(len(lista)):
        if lista[i] == elemento:              
            indice = i
    return indice

def verifica_lado(a, b, c):
    if abs(b - c) < a and a < b + c:
        return True
    else:
        return False

def triang_eh_valido(a,b,c):
    if verifica_lado(a, b, c) and verifica_lado(b, a, c) and verifica_lado(c, a, b):   
        return True
    else:
        return False

def semiperimetro(a, b, c):
    return (a + b + c)/2

def area_triangulo(a,b,c):
    if triang_eh_valido:
        p = semiperimetro(a,b,c)
        return math.sqrt((p * (p - a) * (p - b) * (p - c)))
    else:
        return 0

def area_circulo(raio):
    return math.pi * raio ** 2

# quando o proprio modulo for executado __name__ = __main_

if __name__ == "__main__":
    # codigo de teste: só vai ser executado se
    # este arquivo for executado, mas não vai acontecer caso seja importado
    pass