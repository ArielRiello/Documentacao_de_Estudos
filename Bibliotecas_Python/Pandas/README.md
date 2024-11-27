# Pandas - Biblioteca Python para Análise de Dados
![panda](panda.png)

**Pandas** é uma biblioteca de código aberto usada para **manipulação e análise de dados** em Python. Ela oferece estruturas de dados flexíveis e ferramentas eficientes para lidar com dados estruturados (como tabelas e séries).

## Estruturas de Dados Principais
- **DataFrame**: Uma tabela bidimensional com rótulos para linhas e colunas, ideal para grandes volumes de dados.
- **Series**: Uma estrutura unidimensional, semelhante a uma lista ou uma única coluna de um DataFrame.

## Funcionalidades Principais
1. **Leitura e Escrita de Dados**:
   - Suporte a formatos como CSV, Excel, JSON, SQL, entre outros.
   - Exemplo: `pd.read_csv("arquivo.csv")`.

2. **Manipulação de Dados**:
   - Seleção, filtragem, atualização e transformação de dados.
   - Adição e remoção de colunas ou linhas.
   - Exemplo: `df["nova_coluna"] = df["coluna1"] + df["coluna2"]`.

3. **Limpeza de Dados**:
   - Tratamento de valores ausentes (NaN).
   - Conversão de tipos de dados.
   - Exemplo: `df.dropna()` para remover linhas com valores nulos.

4. **Análise Estatística**:
   - Cálculo de estatísticas como médias, somas e contagens.
   - Exemplo: `df.describe()`.

5. **Agrupamento e Operações em Lote**:
   - Agrupamento de dados por categorias.
   - Exemplo: `df.groupby("categoria").sum()`.

6. **Visualização de Dados**:
   - Integração com bibliotecas como Matplotlib e Seaborn para gráficos.
   - Exemplo: `df.plot()`.

## Por Que Usar Pandas?
- **Flexibilidade**: Permite lidar com dados tabulares e não tabulares de forma eficiente.
- **Alto Desempenho**: Operações vetorizadas otimizadas para grandes volumes de dados.
- **Facilidade de Integração**: Suporte a diversas bibliotecas e formatos de dados.

Pandas é amplamente utilizado em **ciência de dados, aprendizado de máquina e inteligência de negócios** para organizar, transformar e analisar dados de maneira eficiente.
