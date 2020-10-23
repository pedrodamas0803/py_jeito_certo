# Um programa que recebe um numero inteiro do usuario e responde se é par

def ehPar(numero):
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