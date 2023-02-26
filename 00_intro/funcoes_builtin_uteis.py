"""
Funções builtin úteis
Python já vem com uma série de funções úteis
https://docs.python.org/3/library/functions.html
"""

# SUM
# Obtem a soma dos elementos de um iterável contendo números
sum([1, 2, 3])
# 6

# MAX
# Retorna o item com maior valor em uma sequência
max([1, 2, 3])
# 3

# MIN
# Retorna o item com menor valor em uma sequência
min([1, 2, 3])
# 1

# LEN
# Retorna o tamanho de uma sequência
len([1, 2, 3])
# 3
len("Bruno")
# 5

# Reversed
# etorna uma sequência invertida

list(reversed([1, 2, 3]))
# [3, 2, 1]

# Sorted
# Retorna uma sequência ordenada alfabeticamente
list(sorted([9, 8, 1, 2, 3]))
# [1, 2, 3, 8, 9]

# Filter
# Aplica um filtro em uma sequência, sendo que o filtro é uma função que deve retornar True ou False
list(filter(str.isdigit, "Bruno987Rocha452"))
# ['9', '8', '7', '4', '5', '2']

# MAP
# Aplica uma função de transformação em cima de uma sequência
list(map(str.upper, ["bruno", "rocha"]))
# ['BRUNO', 'ROCHA']

# All
# Retorna True se todos os elementos da sequência forem avaliados para True
valores = [True, True, False]
all(valores)
# False
# Atenção: all([]) é True

# Any
# Retorna True se pelo menos um elemento da lista for avaliada para True
valores = [True, True, False]
any(valores)
# True

# Enumerate
# Retorna um objeto iteravél que fornece a numeração de itens de uma sequência
nomes = ["Bruno", "Joao", "Maria", "Sofia"]
for num, nome in enumerate(nomes):
    print(num, nome)
# 0 Bruno
# 1 Joao
# 2 Maria
# 3 Sofia

for num, nome in enumerate(nomes, start=5):
    print(num, nome)
# 5 Bruno
# 6 Joao
# 7 Maria
# 8 Sofia

# ZIP
# Junta 2 sequências em pares

colunas = ["nome", "sobrenome"]
dados = ["Bruno", "Rocha"]
zip(colunas, dados)
# Out[38]: <zip at 0x7fa4c570ba00>
list(zip(colunas, dados))
# [('nome', 'Bruno'), ('sobrenome', 'Rocha')]
dict(zip(colunas, dados))
# {'nome': 'Bruno', 'sobrenome': 'Rocha'}
