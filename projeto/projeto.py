# nome, titulo, data_nasc, mae, pai
def solicitar_dados():
    nome = input('Nome: ')
    titulo = input('Titulo de eleitor: ')
    nascimento = input('Data de nascimento: ')
    mae = input('Nome da mãe: ')
    pai = input('Nome do pai: ')
    votou = input('Votou na ultima eleição? (S/N)')
    dados = (nome, titulo, nascimento, mae, pai, votou)
    return dados

def criar_base_dados(caminho):

    colunas = ['nome',  'mae', 'pai', 'data_nasc', 'titulo', 'votou']

    arquivo = open(caminho, 'w')
    # JEITO PUNK
    # linha = ''
    # for coluna in colunas:
    #     if 
    #     linha = linha + f'{coluna}, '
    # print(linha)

    linha = ','.join(colunas)
    arquivo.write(linha + '\n')
    arquivo.close()

def cadastrar_eleitor(dados, caminho = 'base_eleitores.csv'):
   
    arquivo = open(caminho, 'a')
    arquivo.write(','.join(dados) + 'n')
    arquivo.close()


criar_base_dados('base_eleitores.csv')

dados_eleitor = solicitar_dados()

cadastrar_eleitor(dados_eleitor)
