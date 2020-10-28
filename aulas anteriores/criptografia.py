
def cifra_cesar(chave, texto):
    cifra = ''
    for c in texto:
        code = ord(c)
        letra = code + chave
        cifra = cifra + chr(letra)
    return cifra

cifra = cifra_cesar(3, 'a')
print(cifra)
