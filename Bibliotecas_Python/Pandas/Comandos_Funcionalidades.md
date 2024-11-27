# Comandos e Funcionalidades do Pandas

### Importação de Dados

Lendo arquivos:

~~~py
#CSV:
pd.read_csv("arquivo.csv")

# Excel:
pd.read_excel("arquivo.xlsx", sheet_name="Planilha1")

# JSON:
pd.read_json("arquivo.json")

# SQL:
pd.read_sql("query", conexao)

# HTML:
pd.read_html("url_ou_arquivo.html")
~~~

