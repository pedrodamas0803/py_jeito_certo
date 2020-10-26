# modulo para lidar com o sistema operacional
import os 

path = 'mensagem.txt'

def read_file(path):
        
    myFile = open(path)
    # path = os.path.join('mensagem.txt')
    # myFile = open(path)
    content = myFile.read()
    print(content)
    myFile.close()

def write_file(path):   
    novo_arquivo = open('mensagem.txt', 'w')
    novo_arquivo.sorted()
    novo_arquivo.write('Em noite de lua cheia, enquanto o canguçu esturra, o guatipuru sobe na carapanaúba?')
    novo_arquivo.close()

arquivo = open(path)
linhas = arquivo.readlines()
ordenadas = sorted(linhas)
arquivo.close()
newFile = open(os.path.join('output', 'ordendo.txt'), 'a')
for l in ordenadas:
    newFile.write(l)
newFile.close()