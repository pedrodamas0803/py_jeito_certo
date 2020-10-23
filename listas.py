# programa recebe uma lista de numeros reais e retorna o maior elemento

num_txt = input('Digite alguns números:\n')
# quebra uma string, no espaço
lista = num_txt.split()

numeros = []

for elem in lista:
    numeros.append(float(elem))

maior = -1E6

for n in numeros:
    if n > maior:
        maior = n

print(lista)
print(numeros)
print(maior)
print(max(numeros))