# Metodos e Funcoes
# Funcao é tudo que retorna um valor 
# Metodo é o que nao retorna = def (declaracao de metodo)

def soma1(a, b):
    return a + b

print(soma1(1, 2))
print(soma1(3, 4))

def sub1 (a, b):
    return a - b

print(sub1(10, 2))

# Classe comeca sempre com maiuscula

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b
    
    def sub(self):
        return self.valor_a - self.valor_b
    
    def mult(self):
        return self.valor_a * self.valor_b
    
    def div(self):
        return self.valor_a / self.valor_b
    
calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.valor_b)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.mult())
print(calculadora.div())