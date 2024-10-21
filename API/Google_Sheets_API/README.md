# Uso da API do Google Sheets com Python

## Passo 1: Configuração do projeto no Google Cloud

1. **Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).**
   - Vá para o console e crie um novo projeto.
2. **Ative a API do Google Sheets.**
   - No Google Cloud Console, ative a API do Google Sheets para o seu projeto.
3. **Ative a API do Google Drive.**
   - Isso é necessário para ter permissão de leitura/escrita em planilhas do Google Sheets.
4. **Crie credenciais para sua aplicação.**
   - Vá para a seção "Credenciais" e crie um ID de cliente OAuth ou uma conta de serviço.
   - Para projetos automatizados (sem interface de usuário), é recomendável usar uma **conta de serviço**.

5. **Baixe o arquivo de credenciais JSON.**
   - Depois de criar as credenciais, faça o download do arquivo JSON e guarde-o em um local seguro do seu projeto.

## Passo 2: Instalação das bibliotecas necessárias

Para trabalhar com a API, você precisará das bibliotecas `gspread` e `google-auth`. Instale-as com o seguinte comando:

~~~bash
pip install gspread google-auth
~~~

## Passo 3: Autenticação e configuração do código

1. **Carregue o arquivo JSON de credenciais da conta de serviço.**
   - O arquivo JSON contém as credenciais necessárias para autenticar a aplicação. Certifique-se de que o arquivo está no caminho correto.

2. **Conceda permissão de acesso à planilha.**
   - Compartilhe a planilha com o e-mail da conta de serviço (encontrado no arquivo JSON) para que o script possa acessar e manipular a planilha.

## Passo 4: Exemplo de Código para Configuração e Acesso

Aqui está um exemplo básico para autenticar e acessar uma planilha do Google Sheets:

~~~python
import gspread
from google.oauth2.service_account import Credentials

# Defina o escopo (permissões) para o Google Sheets e Drive
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Carregue as credenciais do arquivo JSON da conta de serviço
credentials = Credentials.from_service_account_file(
    "caminho/para/seu/arquivo-de-credenciais.json",
    scopes=scopes
)

# Autenticação com o gspread usando as credenciais
gc = gspread.authorize(credentials)

# Acesse a planilha pelo nome
planilha = gc.open("Nome_da_sua_Planilha")

# Selecione a primeira aba da planilha
aba = planilha.sheet1

# Exemplo: Ler valores da primeira linha para verificar se a configuração está correta
valores = aba.row_values(1)
print(valores)
~~~

## Passo 5: Verificação e Resolução de Problemas

1. **Erro de Permissão:**
   - Se você encontrar um erro de permissão, verifique se a planilha foi compartilhada com o e-mail da conta de serviço.
   
2. **Arquivo de Credenciais Inválido:**
   - Verifique se o caminho para o arquivo JSON de credenciais está correto e se o arquivo contém as informações necessárias.
   
3. **Bibliotecas Não Instaladas:**
   - Certifique-se de ter instalado corretamente as bibliotecas `gspread` e `google-auth`.

---

Com esses passos, você terá configurado e autenticado corretamente o acesso à API do Google Sheets usando Python.
