lista = [1, 2]
try:
    div = 10 / 1
    numero = lista[1]
    
except ZeroDivisionError:
    print('Não é possivel dividir por zero')
except IndexError:
    print('Erro ao acessar indice da lista')
except BaseException as ex:
    print('ERROR: {}'.format(ex))
else:
    print('Executa quando nao ocorre nenhum erro')
finally:
    print('Sempre executa')