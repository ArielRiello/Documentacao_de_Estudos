from datetime import date, time, datetime

data_atual = date.today()
print(type(data_atual))
data_atual_str = data_atual.strftime('%d/%m/%Y')
print(type(data_atual_str))

print(data_atual.strftime('%d/%m/%Y'))
print(data_atual.strftime('%A/%B/%Y'))

horario = time(hour=15, minute=10, second=10)
print(horario.strftime('%H:%M:%S'))

data = datetime.now()
print(data)
print(data.strftime('%d/%m/%Y'))
print(data.day)
print(data.year)

tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
print(tupla[data.weekday()])

data_criada = datetime(1996, 11, 3, 12, 30, 00)
print(data_criada)
print(data_criada.strftime('%c'))

data_string = '03/11/1996'
data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
print(data_convertida)