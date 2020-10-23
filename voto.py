

def voto_eleitoral(idade):
    if idade >= 18 and idade < 18 or idade >= 70:
        return 'facultativo'
    elif idade < 16:
        return 'proibido'
    else:
        return 'obrigatório'

idade = int(input('Digite a idade: '))

print(voto_eleitoral(idade))