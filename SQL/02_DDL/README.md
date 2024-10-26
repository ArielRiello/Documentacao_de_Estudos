# DDL (Data Definition Language)

## 1. O que é DDL?
- A DDL (Data Definition Language) é uma parte do SQL usada para definir e modificar a estrutura de bancos de dados e tabelas.

- Inclui comandos que permitem criar, alterar e excluir bancos de dados e objetos, como tabelas e índices.

## 2. Comandos Principais do DDL

### CREATE
- Usado para criar novos bancos de dados, tabelas, índices, etc.

- Exemplo: Criar uma tabela chamada `Clientes`.

~~~sql
CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    cidade VARCHAR(50)
);
~~~

### ALTER

- Usado para modificar a estrutura de tabelas existentes, como adicionar, remover ou modificar colunas.
    
- Exemplo: Adicionar uma coluna chamada `telefone` à tabela `Cliente`

~~~sql
ALTER TABLE Clientes
ADD telefone VARCHAR(15);
~~~

- Exemplo: Modificar o tipo de dados da coluna `email`.

~~~sql
ALTER TABLE Clientes
MODIFY email VARCHAR(150);
~~~

### DROP

- Usado para excluir bancos de dados, tabelas ou outros objetos do banco de dados.

- Exemplo: Excluir a tabela `Clientes`.

~~~sql
DROP TABLE Clientes;
~~~

### TRUNCATE

- Usado para remover todos os registros de uma tabela, mas mantendo sua estrutura.

- Exemplo: Limpar todos os dados da tabela `Clientes`.

~~~sql
TRUNCATE TABLE Clientes;
~~~

## 3. Trabalhando com Restrições

- As restrições são usadas para definir regras para os dados em uma tabela. Alguns exemplos de restrições comuns:

    - **NOT NULL**: Garante que uma coluna não pode ter valores nulos.
    
    - **UNIQUE**: Garante que todos os valores em uma coluna sejam diferentes.
    
    - **PRIMARY KEY**: Identifica de forma exclusiva cada registro em uma tabela.
    
    - **FOREIGN KEY**: Estabelece um relacionamento entre duas tabelas.
    
    - **CHECK**: Garante que os valores em uma coluna atendam a uma condição específica.
    
    - **DEFAULT**: Define um valor padrão para uma coluna.

~~~sql
CREATE TABLE Produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) CHECK (preco > 0),
    categoria_id INT,
    CONSTRAINT fk_categoria FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);
~~~

---