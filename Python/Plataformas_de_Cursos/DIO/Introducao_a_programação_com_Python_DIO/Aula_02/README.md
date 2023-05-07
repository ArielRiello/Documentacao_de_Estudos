# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***
---
###  **Aula 02 - O que são variáveis e como manipulá-las através de operadores aritméticos e interação com usuário**
---
**Sintaxe Bãsicas**

A sintaxe básica de Python é relativamente simples e fácil de entender. Aqui estão alguns dos elementos básicos da sintaxe de Python:

* Indentação: a indentação é usada para indicar blocos de código, em vez de chaves ou palavras-chave. A convenção é usar quatro espaços para cada nível de indentação.

* Variáveis: as variáveis em Python são criadas atribuindo um valor a um nome. O tipo da variável é determinado automaticamente com base no valor atribuído.

* Operadores: Python suporta uma ampla variedade de operadores aritméticos, lógicos e relacionais, incluindo +, -, *, /, %, <, >, <=, >=, == e !=.

* Estruturas de controle: Python usa instruções de controle de fluxo, como if, else e while, para controlar o fluxo de execução do programa.

* Funções: as funções em Python são definidas usando a palavra-chave def seguida pelo nome da função, uma lista de argumentos entre parênteses e um bloco de código indentado que define o corpo da função.

* Esses são apenas alguns dos elementos básicos da sintaxe de Python. Python é uma linguagem de programação muito versátil e pode ser usada em uma ampla variedade de aplicações, desde scripts simples até projetos de grande escala.
---

**Variãveis**

Variáveis em Python são utilizadas para armazenar valores que podem ser usados em operações e expressões. As variáveis em Python são criadas quando um valor é atribuído a um nome. Python é uma linguagem de tipagem dinâmica, o que significa que o tipo de uma variável é determinado automaticamente com base no valor que é atribuído a ela.

Em Python, as variáveis são case-sensitive, o que significa que uma variável com nome "x" é diferente de uma variável com nome "X". Além disso, as variáveis podem ter nomes compostos de letras, números e underscores, mas não podem começar com um número.

Para atribuir um valor a uma variável em Python, você usa o operador "=" como neste exemplo:

~~~Python
x = 10
y = x + 5
~~~
---

**Interação com usuário**

Para realizar a interação com o usuário em Python, podemos utilizar a função input(), que permite que o usuário digite uma entrada a partir do teclado e essa entrada seja armazenada em uma variável.

Ex:
~~~Python
nome = input("Digite seu nome: ")
print("Bem-vindo,", nome, "!")
~~~
---

**Codigo feito em aula:**

~~~Python
a = int(input("Informe um valor: "))
b = int(input("Informe outro valor: "))

soma = a + b
sub = a - b
mult = a * b
div = a / b
restoDiv = a % b

print(soma)
print("soma: {} - sub: {}".format(soma, sub))
print("soma: {soma} - \nsub: {sub}".format(soma=soma, sub=sub))
print(sub)
print(mult)
print(div)
print(restoDiv)

print(type(soma))

print("soma: "+ str(soma))

print(div) #Retorna um float
print(int(div)) # Arredonda para um inteiro

x = "1"
soma2 = int(x) + 1
print(soma2)
~~~
---