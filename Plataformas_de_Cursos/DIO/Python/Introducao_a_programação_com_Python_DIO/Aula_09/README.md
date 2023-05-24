# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 09 - Gere, copie, mova, escreva e leia informações de arquivos externos**

---

Em Python, você pode manipular arquivos externos usando as funções do módulo os e do módulo shutil, além das funções integradas de leitura e escrita de arquivos.

Para abrir um arquivo em Python, você pode usar a função open(), que retorna um objeto de arquivo que você pode usar para ler ou escrever no arquivo. A sintaxe para abrir um arquivo é:

~~~Python
arquivo = open('caminho_do_arquivo', 'modo')
~~~

Onde caminho_do_arquivo é o caminho para o arquivo que você deseja abrir e modo é a forma como você deseja abrir o arquivo (por exemplo, para leitura, escrita, etc.). Os modos de abertura mais comuns são:

* 'r': abrir o arquivo para leitura (modo padrão)
* 'w': abrir o arquivo para escrita (se o arquivo já existir, ele será apagado)
* 'a': abrir o arquivo para adicionar conteúdo ao final do arquivo (se o arquivo não existir, ele será criado)
* 'x': criar o arquivo para escrita (se o arquivo já existir, uma exceção será lançada)
Por exemplo, para abrir um arquivo chamado arquivo.txt para leitura, você pode escrever:

~~~Python
arquivo = open('arquivo.txt', 'r')
~~~

Depois de abrir um arquivo, você pode ler o seu conteúdo usando o método read() ou ler o arquivo linha por linha usando o método readline() ou readlines(). Por exemplo, para ler todo o conteúdo de um arquivo, você pode escrever:

~~~Python
conteudo = arquivo.read()
print(conteudo)
~~~

Para escrever conteúdo em um arquivo aberto para escrita ou adição, você pode usar o método write(). Por exemplo, para escrever a string "Olá, mundo!" em um arquivo, você pode escrever:

~~~Python
arquivo.write('Olá, mundo!')
~~~

Depois de escrever ou ler o conteúdo de um arquivo, é importante fechar o arquivo usando o método close() para garantir que todos os recursos do sistema operacional sejam liberados corretamente. Por exemplo, para fechar o arquivo arquivo.txt, você pode escrever:

~~~Python
arquivo.close()
~~~

Além das funções básicas de leitura e escrita de arquivos, o módulo os e o módulo shutil fornecem várias funções para manipular arquivos externos, incluindo:

* os.rename() 
    * renomeia um arquivo ou diretório
* os.remove() 
    * remove um arquivo
* os.mkdir() 
    * cria um novo diretório
* os.rmdir()
    * remove um diretório vazio
* os.listdir()
    * lista o conteúdo de um diretório
* shutil.copy()
    * copia um arquivo de um local para outro
* shutil.move()
    * move um arquivo de um local para outro


Por exemplo, para copiar um arquivo chamado arquivo.txt para um novo arquivo chamado copia.txt, você pode escrever:

~~~Python
import shutil

shutil.copy('arquivo.txt', 'copia.txt')
~~~

---

**Codigos feitos em aula:** *Aula_09.py*

---