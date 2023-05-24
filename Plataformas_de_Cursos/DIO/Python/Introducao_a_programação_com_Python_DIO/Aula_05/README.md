# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 05 - Como organizar os dados em uma lista ou tupla e realizar operações com elas**
---

Em Python, as listas e tuplas são estruturas de dados que permitem armazenar um conjunto de valores. Para criar uma lista ou tupla, basta utilizar colchetes [] para listas ou parênteses () para tuplas e separar os elementos com vírgulas.

Exemplo:
~~~Python
# lista
minha_lista = [1, 2, 3, 4, 5]

# tupla
minha_tupla = (1, 2, 3, 4, 5)

~~~

Uma vez criada a lista ou tupla, podemos realizar diversas operações com elas, como acessar elementos específicos, adicionar ou remover elementos, ordená-las, entre outras.

Para acessar um elemento específico da lista ou tupla, utilizamos a sintaxe de colchetes e informamos o índice do elemento desejado. É importante lembrar que os índices em Python começam em 0.

Exemplo:
~~~Python
# acessando o segundo elemento da lista
print(minha_lista[1]) # 2

# acessando o terceiro elemento da tupla
print(minha_tupla[2]) # 3

~~~

Para adicionar um novo elemento à lista, podemos utilizar o método append().

Exemplo:

~~~Python
# adicionando um novo elemento à lista
minha_lista.append(6)
print(minha_lista) # [1, 2, 3, 4, 5, 6]
~~~

Para remover um elemento específico da lista, podemos utilizar o método remove().

Exemplo:
~~~Python
# removendo um elemento da lista
minha_lista.remove(3)
print(minha_lista) # [1, 2, 4, 5, 6]
~~~

Para ordenar uma lista, podemos utilizar o método sort(). Para ordenar uma tupla, podemos utilizar a função sorted().

Exemplo:

~~~Python
# ordenando a lista
minha_lista.sort()
print(minha_lista) # [1, 2, 4, 5, 6]

# ordenando a tupla
minha_tupla_ordenada = sorted(minha_tupla)
print(minha_tupla_ordenada) # [1, 2, 3, 4, 5]
~~~


Essas são apenas algumas das operações que podemos realizar com listas e tuplas em Python. Há muitas outras funções e métodos disponíveis para manipular essas estruturas de dados de forma eficiente e flexível.

---

**Codigos feitos em aula:**

1. 
~~~Python
lista = [1, 3, 5 , 7]
lista_animal = ["cachorro", "gato", "elefante"]
print(lista_animal[1])

for x in lista_animal:
    print(x)

soma = 0 
for x in lista:
    print(x)
    soma += x
print(soma)

print(sum(lista))

print(max(lista))

print(min(lista_animal))

if "lobo" in lista_animal:
    print("Existe lobo na lista")
else:
    print("Não existe lobo na lista")
    lista_animal.append("lobo") # Adiciona a primeira posicao
    print(lista_animal)

lista_animal.pop(3) # Retira 3 posicao da lista

lista_animal.remove("gato")

lista2 = [12, 10, 7, 5]
lista2.sort()
print(lista2)

lista2.reverse()
print(lista2)
~~~

2.
~~~Python
# Tupla
# As tuplas são imutaveis, diferente das listas

tupla = (1, 2, 12, 14) # Usa () ao inves de []
print(tupla)

print(len(tupla))

lista = [1, 2, 3]
tupla = lista

print(tupla)
~~~
---