
def save(mensagem):
    arquivo = open('mensagem.txt', 'w')
    arquivo.write(mensagem)
    arquivo.close()

def podeVotar(idade):
    if idade >= 18 and idade < 70:
       return 'obrigatorio'
        # print(f'Com {idade} anos, seu voto é obrigatório')
    elif idade >= 16:
        return 'facultativo'
        # print(f'Com {idade} anos, seu voto é facultativo')
    else:
        return 'proibido'
        # print(f'Com {idade} anos, você NÂO pode votar')

idade  =  int(input('Digite sua idade: '))
resposta = podeVotar(idade)
save(f'Com {idade} anos, seu voto é {resposta}')