import shutil

# 'w' - Faz uma nova escrita (sobre-escreve o existente)
# 'a' - Escreve na linha seguinte
# 'r' - Le o aqruivo

def escrever_arquivo(texto):
    diretorio = 'teste.txt'
    arquivo = open(diretorio, 'w') 
    arquivo.write(texto) 
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto) 
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def copia_arquivo(nome_arquio):
    shutil.copy(nome_arquio, 'teste2.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'local onde sera enviado o arquivo')

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    atualizar_arquivo('Segunda linha.\n')
    ler_arquivo('teste.txt')
    copia_arquivo('teste.txt')