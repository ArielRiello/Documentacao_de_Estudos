# **Introdução à programação com Python**
*Documentação de estudos **Ariel Riello***

---

###  **Aula 10 - Aprenda a utilizar informações de data, horário e relacionar datas diferentes**

---

Em Python, você pode trabalhar com informações de data e hora usando o módulo datetime. Esse módulo fornece várias classes para representar datas, horários e intervalos de tempo.

A classe mais básica para trabalhar com datas é a classe date, que representa uma data no formato ano-mês-dia. Para criar um objeto date, você pode usar o construtor da classe passando o ano, o mês e o dia como argumentos. Por exemplo:

~~~Python
from datetime import date

# cria um objeto date para representar 26 de abril de 2023
data1 = date(2023, 4, 26)
~~~

Você pode obter informações sobre uma data usando os atributos year, month e day. Por exemplo:

~~~Python
print(data1.year)   # 2023
print(data1.month)  # 4
print(data1.day)    # 26
~~~

A classe time representa um horário no formato hora-minuto-segundo-microssegundo. Você pode criar um objeto time usando o construtor da classe passando a hora, o minuto, o segundo e o microssegundo como argumentos. Por exemplo:

~~~Python
from datetime import time

# cria um objeto time para representar 14h30min45s
horario1 = time(14, 30, 45)
~~~

Você pode obter informações sobre um horário usando os atributos hour, minute, second e microsecond. Por exemplo:

~~~Python
print(horario1.hour)   # 14
print(horario1.minute) # 30
print(horario1.second) # 45
~~~

A classe datetime representa uma data e um horário combinados. Você pode criar um objeto datetime usando o construtor da classe passando a data e o horário como argumentos. Por exemplo:

~~~Python
from datetime import datetime

# cria um objeto datetime para representar 26 de abril de 2023 às 14h30min45s
data_hora1 = datetime(2023, 4, 26, 14, 30, 45)
~~~

Você pode obter informações sobre um objeto datetime usando os mesmos atributos que para as classes date e time. Além disso, você pode obter o dia da semana usando o atributo weekday(), que retorna um número de 0 a 6, onde 0 é segunda-feira e 6 é domingo. Por exemplo:

~~~Python
print(data_hora1.weekday())  # 2 (quarta-feira)
~~~

Para calcular a diferença entre duas datas ou horários, você pode usar o operador de subtração -, que retorna um objeto timedelta representando o intervalo de tempo entre os dois objetos. Por exemplo:

~~~Python
from datetime import timedelta

# cria um objeto timedelta para representar um intervalo de 1 hora e 30 minutos
intervalo1 = timedelta(hours=1, minutes=30)

# calcula a hora 2 horas e 15 minutos após a hora 14h30min45s
horario2 = horario1 + timedelta(hours=2, minutes=15)
~~~

Você pode somar ou subtrair um objeto timedelta de um objeto date, time ou datetime para calcular uma nova data ou horário. Por exemplo:

~~~Python
# calcula a data 10 dias após a data1
data2
~~~

---

**Codigos feitos em aula:** *Aula_10.py*

---