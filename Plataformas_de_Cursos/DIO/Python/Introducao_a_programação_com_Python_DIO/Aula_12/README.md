# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 12 - FINAL - Instalando e utilizando pacotes em Python e realizar requisição com requests**

---

Python possui um gerenciador de pacotes chamado pip (que é instalado junto com o Python em versões mais recentes). Para instalar pacotes em Python, basta usar o comando pip install <nome_do_pacote> no terminal ou prompt de comando.

Por exemplo, para instalar o pacote requests, que é utilizado para fazer requisições HTTP em Python, basta digitar o comando abaixo no terminal:

~~~
pip install requests
~~~

Após instalar o pacote, você pode importá-lo em seu código Python utilizando a instrução import requests. Em seguida, você pode utilizar as funções e classes do pacote.

Um exemplo de como realizar uma requisição HTTP utilizando o pacote requests em Python é mostrado abaixo:

~~~Python
import requests

# realiza uma requisição GET para o site do Google
response = requests.get("https://www.google.com")

# verifica o código de status da resposta
if response.status_code == 200:
    print("Requisição bem sucedida!")
else:
    print("Ocorreu um erro:", response.status_code)
~~~

Neste exemplo, a função requests.get() é utilizada para realizar uma requisição GET para o site do Google. Em seguida, é verificado o código de status da resposta utilizando a propriedade status_code do objeto response. Se o código de status for igual a 200, significa que a requisição foi bem sucedida e uma mensagem é exibida. Caso contrário, é exibida uma mensagem de erro com o código de status retornado.

O pacote requests oferece muitas outras funcionalidades, como realizar requisições POST, enviar cabeçalhos personalizados, fazer download de arquivos, entre outras.

Tais como:

* Enviar parâmetros de consulta em uma requisição GET usando o parâmetro params.
* Enviar dados em uma requisição POST usando o parâmetro data.
* Enviar arquivos em uma requisição POST usando o parâmetro files.
* Enviar cabeçalhos personalizados em uma requisição usando o parâmetro headers.
* Gerenciar cookies em uma sessão HTTP usando a classe Session.
* Lidar com redirecionamentos automáticos em uma requisição usando o parâmetro allow_redirects.
* Definir timeouts para a requisição usando o parâmetro timeout.

A seguir, um exemplo resumido de como utilizar algumas dessas funcionalidades:

~~~Python

import requests

# enviar parâmetros de consulta em uma requisição GET
params = {"q": "python", "page": 2}
response = requests.get("https://www.google.com/search", params=params)

# enviar dados em uma requisição POST
data = {"username": "joao", "password": "123"}
response = requests.post("https://www.example.com/login", data=data)

# enviar arquivos em uma requisição POST
files = {"file": open("example.txt", "rb")}
response = requests.post("https://www.example.com/upload", files=files)

# enviar cabeçalhos personalizados em uma requisição
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get("https://www.example.com", headers=headers)

# gerenciar cookies em uma sessão HTTP
session = requests.Session()
session.post("https://www.example.com/login", data=data)
response = session.get("https://www.example.com/dashboard")

# lidar com redirecionamentos automáticos em uma requisição
response = requests.get("http://www.example.com", allow_redirects=False)

# definir timeouts para a requisição
response = requests.get("https://www.example.com", timeout=5)
~~~

Estes são apenas alguns exemplos das funcionalidades que o pacote requests em Python oferece. É importante consultar a documentação oficial do pacote para uma lista completa de funcionalidades e exemplos mais detalhados.

---

**Codigos feitos em aula:** *Aula_12.py*

---