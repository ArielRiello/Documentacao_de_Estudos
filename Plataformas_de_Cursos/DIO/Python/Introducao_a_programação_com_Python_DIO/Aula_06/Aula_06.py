conjunto = {1, 2, 3, 4}
conjunto.add(5) 
conjunto.discard(2)
print(conjunto)

print("------------")

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}
conjuto12 = conjunto1.union(conjunto2) # Junta os dois conjuntos
print(conjuto12)

conjunto_interseccao = conjunto1.intersection(conjunto2) # Mosta o que tem em comum nos 2 conjuntos
print(conjunto_interseccao)

conjunto_diferenca = conjunto1.difference(conjunto2) # Mostra as diferencas
print(conjunto_diferenca)

conjunto_dif_simetrico = conjunto1.symmetric_difference(conjunto2) # O que contem em um que nao contem no outro
print(conjunto_dif_simetrico)

print("------------")

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)

conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

print("------------")

lista = ["cachorro", "cachorro", "gato", "gato", "elefante"]
print(lista)
conjuto_animais = set(lista)
print(conjuto_animais)
lista_animais = list(conjuto_animais)
print(lista_animais)