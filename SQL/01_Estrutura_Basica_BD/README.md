# Estrutura Básica de Bancos de Dados

## 1. Bancos de Dados, Tabelas, Colunas e Registros
- **Banco de Dados**: Um conjunto organizado de dados que são armazenados e gerenciados eletronicamente. Em um banco de dados relacional, os dados são organizados em tabelas.

- **Tabelas**: São estruturas que armazenam dados em formato tabular, com linhas e colunas. Cada tabela representa uma entidade específica (ex.: clientes, produtos).

- **Colunas (Campos)**: Cada coluna representa um atributo ou característica dos dados. Por exemplo, uma tabela de clientes pode ter colunas como `nome`, `email` e `telefone`.

- **Linhas (Registros)**: Cada linha é uma entrada individual na tabela, representando um conjunto completo de informações para uma entidade. Por exemplo, uma linha na tabela de clientes pode representar um cliente específico.

## 2. Tipos de Dados
Cada coluna em uma tabela tem um tipo de dado que define o tipo de valor que pode ser armazenado. Exemplos de tipos de dados:
- **INT**: Números inteiros (ex.: 1, 42).

- **VARCHAR(n)**: Cadeia de caracteres de comprimento variável, com limite `n` (ex.: "João", "Maria").

- **DATE**: Datas (ex.: `2024-10-26`).

- **FLOAT/DECIMAL**: Números com casas decimais (ex.: 3.14).

- **BOOLEAN**: Valores verdadeiro/falso (`true` ou `false`).

## 3. Chaves Primárias e Estrangeiras
- **Chave Primária (Primary Key)**: Um identificador exclusivo para cada registro em uma tabela. Ela garante que cada linha possa ser identificada de forma única. Exemplos comuns incluem IDs numéricos sequenciais.

- **Chave Estrangeira (Foreign Key)**: Um campo que cria uma relação entre duas tabelas. Ele referencia a chave primária de outra tabela, estabelecendo uma conexão entre as duas. Isso permite a integridade referencial no banco de dados.

## 4. Normalização de Dados
A **normalização** é o processo de organizar os dados em um banco de dados para reduzir a redundância e melhorar a integridade dos dados. Isso é feito seguindo certas regras:
- **1ª Forma Normal (1NF)**: Cada campo deve conter apenas um valor por registro.

- **2ª Forma Normal (2NF)**: Todos os campos devem depender da chave primária.

- **3ª Forma Normal (3NF)**: Todos os campos devem depender diretamente da chave primária e não de outros campos.

A normalização é importante para garantir que o banco de dados seja eficiente e livre de anomalias de atualização.

## 5. Exemplo de Estrutura de Tabela
~~~sql
CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(15),
    data_de_cadastro DATE
);
~~~

- No exemplo acima:

  - A tabela `Clientes` possui colunas `id`, `nome`, `email`, `telefone` e `data_de_cadastro`.
      
  - `id` é a chave primária que identifica de forma única cada cliente.
      
  - `nome` é obrigatório (indicado pelo `NOT NULL`).
      
  - Os tipos de dados foram escolhidos para se adequar às informações que serão armazenadas.

---