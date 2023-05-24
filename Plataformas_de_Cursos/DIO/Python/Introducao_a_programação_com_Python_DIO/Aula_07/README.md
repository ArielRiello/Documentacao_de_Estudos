# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 07 - Construindo métodos, funções e classes em Python**
---


Python é uma linguagem de programação orientada a objetos e, como tal, permite a criação de métodos, funções e classes para organizar o código em unidades lógicas reutilizáveis. 

Segue abaixo exemplos de como criar cada uma dessas estruturas:

---

**Métodos**

Os métodos são funções definidas dentro de uma classe e que operam nos objetos dessa classe. Para criar um método em Python, é necessário definir uma função dentro da classe e usar a palavra-chave "self" como primeiro parâmetro, que representa o objeto que está chamando o método. Segue um exemplo:


~~~Python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"Este é um {self.modelo} da marca {self.marca}, fabricado em {self.ano}."
~~~


Nesse exemplo, criamos a classe "Carro", que tem um método chamado "descricao" que retorna uma string com informações sobre o carro.

---

**Funções**


As funções em Python são definidas fora de classes e podem receber argumentos e retornar valores. Para criar uma função em Python, basta usar a palavra-chave "def", seguida do nome da função e seus argumentos, se houverem. Veja um exemplo:

~~~Python
def soma(a, b):
    return a + b
~~~


Nesse exemplo, criamos uma função chamada "soma" que recebe dois argumentos e retorna a soma deles.

---

**Classes**

As classes em Python são estruturas que permitem agrupar dados e funções relacionados em uma unidade lógica. Para criar uma classe em Python, é necessário usar a palavra-chave "class", seguida do nome da classe e dois pontos. Dentro da classe, podemos definir atributos (variáveis) e métodos (funções). Segue um exemplo:

~~~Python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
~~~

Nesse exemplo, criamos a classe "Retangulo", que tem atributos "largura" e "altura" e dois métodos, "area" e "perimetro", que calculam a área e o perímetro do retângulo, respectivamente.

---

Esses são apenas alguns exemplos de como criar métodos, funções e classes em Python. A linguagem oferece muitas outras possibilidades e recursos para organizar o código em unidades lógicas reutilizáveis e facilitar o desenvolvimento de programas complexos.

---
**Codigos feitos em aula:** *Aula_07_Ex1.py / Aula_07_Ex2.py / Aula_07_Ex3.py*

---
