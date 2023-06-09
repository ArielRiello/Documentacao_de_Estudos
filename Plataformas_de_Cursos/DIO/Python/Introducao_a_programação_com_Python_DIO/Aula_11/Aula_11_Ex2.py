
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: 
    try:
        x = int(input('Entre com um nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota nao pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota nao pode ser menor que zero')
        break
    except ValueError:
        print('Deve-se digitar apenas numeros')
    except InputError as ex:
        print(ex)