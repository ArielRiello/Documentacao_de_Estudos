# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 08 - Lidando com módulos, importação de classes, métodos e construção de funções anônimas (lambda)**

---

**Módulos e Importação de Classes**

Módulos em Python são arquivos contendo código Python que podem ser importados em outros arquivos Python. Eles permitem reutilizar código e tornar o seu programa mais modular e fácil de manter. Para importar um módulo em Python, você pode usar a palavra-chave import seguida do nome do módulo. Por exemplo, para importar o módulo math, você pode escrever:

~~~Python
import math
~~~

Depois de importar um módulo, você pode usar as classes, funções e variáveis definidas no módulo. Por exemplo, para usar a função sqrt (raiz quadrada) do módulo math, você pode escrever:

~~~Python
import math

x = math.sqrt(25)
print(x)  # saída: 5.0
~~~

Além disso, você pode importar apenas uma classe ou função específica de um módulo usando a sintaxe from modulo import nome. Por exemplo, para importar apenas a função sqrt do módulo math, você pode escrever:

~~~Python
from math import sqrt

x = sqrt(25)
print(x)  # saída: 5.0
~~~

---

**Funções Anônimas** *lambda*

Funções anônimas, também conhecidas como lambda functions, são funções que não têm um nome definido e podem ser criadas usando a palavra-chave lambda. Elas são úteis quando você precisa de uma função temporária para realizar uma tarefa simples. A sintaxe para criar uma função lambda é:

~~~Python
lambda argumentos: expressão
~~~

Por exemplo, para criar uma função lambda que recebe um número e retorna o seu dobro, você pode escrever:

~~~Python
dobro = lambda x: x * 2
print(dobro(5))  # saída: 10
~~~

As funções lambda podem ser usadas em qualquer lugar em que você possa usar uma função regular, como em uma expressão map, filter ou reduce.

---

**Classe**

Por fim, para criar uma classe em Python, você pode usar a palavra-chave class seguida pelo nome da classe. Dentro da classe, você pode definir métodos (funções) e variáveis de instância. Por exemplo, para criar uma classe Pessoa com um método dizer_ola, você pode escrever:

~~~Python
class Pessoa:
    def dizer_ola(self):
        print("Olá!")

p = Pessoa()
p.dizer_ola()  # saída: "Olá!"
~~~


Para importar uma classe definida em um arquivo Python separado, você pode usar a sintaxe from modulo import Classe. Por exemplo, se tivermos uma classe Pessoa definida no arquivo pessoa.py, você pode importá-la usando:

~~~Python
from pessoa import Pessoa

p = Pessoa()
p.dizer_ola()  # saída: "Olá!"
~~~

---

**Codigos feitos em aula:** *Aula_08_Ex1.py / Aula_08_Ex2.py / Aula_08_Ex3.py / Aula_08_Ex4.py*

---