# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 06 - Organizando conjuntos e subconjuntos de elementos em Python**
---


Em Python, podemos organizar conjuntos e subconjuntos de elementos usando listas e dicionários.

~~~Python
# Criando uma lista de números inteiros
numeros = [1, 2, 3, 4, 5]

# Criando uma lista de strings
nomes = ["Maria", "João", "Ana", "Pedro"]

# Acessando o segundo e terceiro elementos da lista "numeros" (subconjunto)
subconjunto_numeros = numeros[1:3] # resultado: [2, 3]

# Criando um dicionário de informações de uma pessoa
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Acessando o valor da chave "idade" do dicionário "pessoa"
idade = pessoa["idade"] # resultado: 30

# Criando um subconjunto do dicionário "pessoa" com apenas as chaves "nome" e "cidade"
subconjunto_pessoa = {"nome": pessoa["nome"], "cidade": pessoa["cidade"]}
~~~

Neste código, estamos organizando conjuntos e subconjuntos de elementos usando listas e dicionários.

Na primeira parte do código, criamos uma lista de números inteiros e uma lista de strings, que são dois exemplos de conjuntos de elementos que podem ser organizados em uma lista. Em seguida, usamos a sintaxe de fatiamento (slicing) para acessar o segundo e terceiro elementos da lista "numeros", criando assim um subconjunto.

Na segunda parte do código, criamos um dicionário com informações sobre uma pessoa, que é um exemplo de conjunto de elementos que pode ser organizado em um dicionário. Usando a sintaxe de chaves e colchetes, acessamos o valor da chave "idade" do dicionário "pessoa".

Por fim, criamos um subconjunto do dicionário "pessoa" com apenas as chaves "nome" e "cidade", usando a sintaxe de chaves e pares chave-valor.

---

**Codigos feitos em aula:** *Aula06.py*

---