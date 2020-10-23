# de uma lista soma dos pares e multiplicacao dos impares

numeros = [1, 3, 2, 4, 6, 3, 9, 3]
from matematica import *

soma = 0
produto = 1
for n in numeros:

    if ehPar(n):
        soma = soma + n
    else:
        produto = produto * n

print('Soma dos pares é ', soma)
print('Produto dos ímpares é', produto)