# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 11 - Gerenciando e criando exceções customizadas com try, except, else e finally**

---

Em Python, é possível gerenciar exceções usando as palavras-chave try, except, else e finally.

O bloco try é usado para envolver o código que pode lançar uma exceção. Dentro do bloco try, você pode colocar o código que deseja executar, e que pode lançar uma exceção. Se a exceção for lançada, o fluxo do programa é interrompido e passa para o bloco except.

O bloco except é usado para lidar com exceções. Você pode especificar o tipo de exceção que deseja lidar dentro do bloco except. Se a exceção especificada ocorrer dentro do bloco try, o bloco except será executado. Dentro do bloco except, você pode colocar o código que deseja executar para lidar com a exceção.

O bloco else é opcional e é executado somente se nenhuma exceção foi lançada no bloco try. Você pode colocar o código que deseja executar quando não ocorrer exceções dentro do bloco else.

O bloco finally também é opcional e é executado sempre, independentemente de ocorrer exceções ou não no bloco try. Você pode colocar o código que deseja executar sempre, como fechar arquivos ou conexões de banco de dados, dentro do bloco finally.

A seguir, um exemplo de como utilizar as palavras-chave try, except, else e finally para gerenciar exceções em Python:

~~~Python
try:
    # código que pode lançar uma exceção
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    resultado = x / y
except ZeroDivisionError:
    # código para lidar com a exceção ZeroDivisionError
    print("Não é possível dividir por zero.")
except ValueError:
    # código para lidar com a exceção ValueError
    print("Digite somente números inteiros.")
else:
    # código para executar se nenhuma exceção foi lançada
    print("O resultado é:", resultado)
finally:
    # código para executar sempre
    print("Fim do programa.")
~~~

Neste exemplo, o bloco try tenta dividir dois números digitados pelo usuário. Se ocorrer uma exceção do tipo ZeroDivisionError, o bloco except ZeroDivisionError é executado, que exibe uma mensagem para o usuário. Se ocorrer uma exceção do tipo ValueError, o bloco except ValueError é executado, que também exibe uma mensagem para o usuário. Se nenhuma exceção ocorrer, o bloco else é executado, que exibe o resultado da divisão. O bloco finally é executado sempre, que exibe uma mensagem para indicar o fim do programa.

---

**Codigos feitos em aula:** *Aula_11_Ex1.py / Aula_11_Ex2.py*

---