# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***
---
###  **Aula 03 - Como criar um código em Python que funcione de acordo com a relação das variáveis**
---
**Condicionais**

Condicionais em Python são estruturas de controle de fluxo que permitem que o código execute diferentes ações com base em uma condição especificada. A condição é geralmente uma expressão booleana que avalia para True ou False.

A estrutura condicional mais comum em Python é o if, que testa uma condição e executa um bloco de código se a condição for verdadeira. Por exemplo:

~~~Python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
~~~

Neste exemplo, a expressão idade >= 18 é avaliada como True e, portanto, o bloco de código dentro do if é executado, exibindo a mensagem "Você é maior de idade.".

Além do if, existem outras estruturas condicionais em Python, como o if-else, que executa um bloco de código se a condição for verdadeira e outro bloco de código se a condição for falsa, e o if-elif-else, que permite testar várias condições e executar diferentes blocos de código com base na primeira condição que for verdadeira.

As estruturas condicionais são uma parte fundamental da linguagem de programação Python e são usadas em uma ampla variedade de aplicações para tomar decisões e controlar o fluxo de execução do programa.

---
**Operadores Lógicos**

Operadores lógicos são usados em Python para avaliar expressões booleanas e produzir um resultado booleano (True ou False). Existem três operadores lógicos principais em Python:

* and: Retorna True se ambas as expressões forem verdadeiras.
* or: Retorna True se pelo menos uma das expressões for verdadeira.
* not: Inverte o resultado da expressão
    * se a expressão for verdadeira, retorna
False; se a expressão for falsa, retorna True.

Esses operadores podem ser usados para criar expressões booleanas mais complexas, que são usadas em estruturas condicionais e loops para controlar o fluxo de execução do programa.

Por exemplo, suponha que queremos verificar se um número está entre 10 e 20 ou se é igual a 30. Podemos usar o operador or para combinar duas expressões booleanas:

~~~Python
numero = 15
if numero >= 10 and numero <= 20 or numero == 30:
    print("O número está entre 10 e 20 ou é igual a 30.")
~~~
---

**Codigo feito em aula:**

1. 
~~~Python
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

if a > b and a > c:
    print("O maior numero é A: ",a)
elif b > a and b > c:
    print("O maior numero é B: ",b)
else:
    print("O maior numero é C: ",c)
~~~

2. 
~~~Python

a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o primeiro valor: "))

resto_a = a % 2 
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print("foi digitado um numero par")
else:
    print("nenhum numero par foi digitado")
~~~

3. 
~~~Python
a = int(input("Primeiro bimestre: "))
b = int(input("Segundo bimestre: "))
c = int(input("Terceiro bimestre: "))
d = int(input("Quarto bimestre: "))

media = (a + b + c + d) / 2

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print("Media: ", media)
else:
    print("foi informado alguma nota errada!")
~~~
---