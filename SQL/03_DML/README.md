# DML (Data Manipulation Language)

## 1. O que é DML?
- DML (Data Manipulation Language) é uma parte do SQL usada para manipular os dados dentro das tabelas de um banco de dados.

- Permite realizar operações como inserção, atualização, exclusão e leitura de dados.

## 2. Comandos Principais do DML

### SELECT
- Usado para consultar e retornar dados de uma tabela.

- Exemplo: Selecionar todos os campos da tabela `Clientes`.

~~~sql
SELECT * FROM Clientes;
~~~

- Selecionar colunas específicas.

~~~sql
SELECT nome, email FROM Clientes;
~~~

- Usar a cláusula `WHERE` para filtrar os resultados.

~~~sql
SELECT * FROM Clientes WHERE cidade = 'São Paulo';
~~~

### INSERT
- Usado para inserir novos registros em uma tabela.

- Exemplo: Inserir um novo cliente na tabela `Clientes`.

~~~sql
INSERT INTO Clientes (id, nome, email, cidade)
VALUES (1, 'João Silva', 'joao@email.com', 'São Paulo');
~~~

### UPDATE
- Usado para atualizar registros existentes em uma tabela.

- Exemplo: Atualizar o nome de um cliente com `id = 1`.

~~~sql
UPDATE Clientes
SET nome = 'João Souza'
WHERE id = 1;
~~~

### DELETE
- Usado para remover registros de uma tabela.

- Exemplo: Excluir um cliente com `id = 1`.

~~~sql
DELETE FROM Clientes
WHERE id = 1;
~~~

## 3. Cláusulas Adicionais do DML

### ORDER BY
- Usada para ordenar os resultados da consulta.

- Exemplo: Ordenar os clientes pelo nome de forma ascendente.

~~~sql
SELECT * FROM Clientes
ORDER BY nome ASC;
~~~

### LIMIT
- Usada para limitar o número de registros retornados pela consulta.

- Exemplo: Selecionar os 5 primeiros clientes.

~~~sql
SELECT * FROM Clientes
LIMIT 5;
~~~

---