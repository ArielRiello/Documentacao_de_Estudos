# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***
---
###  **Aula 04 - Como criar laços de repetição em Python**
---
**WHILE**

Em Python, podemos criar laços de repetição usando as estruturas while ou for.

A estrutura while executa um bloco de código enquanto uma determinada condição é verdadeira. Por exemplo:

~~~Python
contador = 0
while contador < 10:
    print(contador)
    contador += 1

~~~

Neste exemplo, o bloco de código dentro do while é executado enquanto a condição contador < 10 for verdadeira. O contador é incrementado a cada iteração, para que o loop eventualmente pare depois de imprimir os números de 0 a 9.

---
**FOR**

Já a estrutura for é usada para iterar sobre uma sequência de valores, como uma lista, tupla ou string. Por exemplo:

~~~Python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
~~~

Neste exemplo, o loop for executa o bloco de código uma vez para cada valor na lista frutas, atribuindo cada valor a variável fruta. O resultado é que cada valor da lista é impresso na tela.

Laços de repetição são uma parte fundamental da programação em Python e são usados em uma ampla variedade de aplicações para automatizar tarefas e processar grandes quantidades de dados.

---

**Codigo feito em aula:**

1. 
~~~Python
for numero in range (101):

    div = 0

    for x in range(1, numero + 1):
        resto = numero % x
        if resto == 0:
            div += 1

    if div == 2:
        print(numero)
~~~

2. 
~~~Python
nota = int(input("Entre com a nota: "))
while nota > 10:
    nota = int(input("Nota invalida, informe uma nota valida: "))
    print(nota)
~~~

---