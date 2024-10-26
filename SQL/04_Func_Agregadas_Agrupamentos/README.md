# Funções Agregadas e Agrupamento

## 1. O que são Funções Agregadas?
- Funções agregadas realizam cálculos em um conjunto de valores e retornam um único valor.

- São usadas frequentemente para gerar estatísticas e relatórios.

### Principais Funções Agregadas:

- **COUNT()**: Conta o número de registros.

- **SUM()**: Calcula a soma de um campo numérico.

- **AVG()**: Calcula a média de um campo numérico.

- **MAX()**: Encontra o maior valor.

- **MIN()**: Encontra o menor valor.

## 2. Exemplos de Uso de Funções Agregadas

### COUNT
- Exemplo: Contar o número total de clientes na tabela `Clientes`.

~~~sql
SELECT COUNT(*) FROM Clientes;
~~~

### SUM
- Exemplo: Calcular a soma dos preços dos produtos.

~~~sql
SELECT SUM(preco) FROM Produtos;
~~~

### AVG
- Exemplo: Calcular a média dos preços dos produtos.

~~~sql
SELECT AVG(preco) FROM Produtos;
~~~

### MAX
- Exemplo: Encontrar o maior valor de preço na tabela `Produtos`.

~~~sql
SELECT MAX(preco) FROM Produtos;
~~~

### MIN
- Exemplo: Encontrar o menor valor de preço na tabela `Produtos`.

~~~sql
SELECT MIN(preco) FROM Produtos;
~~~

## 3. Agrupamento com GROUP BY
- O `GROUP BY` é usado para agrupar registros que têm valores em comum em colunas específicas.

- Quando usado com funções agregadas, ele permite realizar cálculos em grupos de registros.

### Exemplo de Agrupamento
- Contar o número de clientes por cidade.

~~~sql
SELECT cidade, COUNT(*) 
FROM Clientes
GROUP BY cidade;
~~~

### Uso de HAVING com GROUP BY
- O `HAVING` é usado para filtrar grupos de resultados, diferentemente do `WHERE`, que filtra linhas.

- Exemplo: Mostrar apenas cidades com mais de 5 clientes.

~~~sql
SELECT cidade, COUNT(*) 
FROM Clientes
GROUP BY cidade
HAVING COUNT(*) > 5;
~~~

---