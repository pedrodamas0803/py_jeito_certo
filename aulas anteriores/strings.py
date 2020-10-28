# verificar se existem caracteres duplicados em strings

def tem_duplicado(palavra):
    vistos = []
    for c in palavra:
        if c in vistos:
            return True
        vistos.append(c)
    return False
if tem_duplicado('pedro'):
    print('Tem duplicado')
else:
    print('Não tem duplicado')