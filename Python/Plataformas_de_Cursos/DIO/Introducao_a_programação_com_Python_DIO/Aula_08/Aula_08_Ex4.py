#Lambda - funcao anonima

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['gato', 'rato']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(5, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

print(type(calculadora))

soma = calculadora['soma']
print(soma(10,5))