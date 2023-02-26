# Random
# Retorna elementos randomicos
import getpass
import uuid
import statistics as st
import functools as ft
import itertools as it
import random

random.random()
0.3416667413859049

random.randint(1, 10)
# 8
random.randint(1, 10)
# 4

random.choice(["red", "green", "blue"])
# 'red'
random.choice(["red", "green", "blue"])
# 'blue'

random.sample([1, 2, 3, 4, 5], 2)
# [4, 5]
random.sample([1, 2, 3, 4, 5], 2)
# [1, 3]

numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
# [5, 2, 4, 6, 1, 3]

# Itertools
# Funções úteis para trabalhar com objetos iteráveis

for item in it.cycle("ABCD"):
    print(item)

list(it.repeat("Bruno", 10))
# ['Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno', 'Bruno']

list(it.accumulate([1, 2, 3, 4, 5]))
# [1, 3, 6, 10, 15]

list(it.product("ABC", repeat=2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

list(it.permutations("ABC"))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

list(it.combinations("ABCDE", 2))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E'), ('D', 'E')]

# Functools
# Funções uteís para manipular funções

print("Bruno", "Rocha")
# Bruno Rocha
myprint = ft.partial(print, sep="---")
myprint("Bruno", "Rocha")
# Bruno---Rocha

# Statistics
# Retorna estatisticas como por exemplo média e mediana.

st.mean([1, 2, 2, 5, 10, 12])
# 5.333333333333333

st.median([1, 2, 2, 5, 10, 12])
# 3.5

# UUID
# Universal Unique ID

uuid.uuid4()
# UUID('db5601e3-5c7c-4fb0-91c4-60f33852e11c')
str(uuid.uuid4())
# '23b92cdb-f79f-41d9-a083-8474c02df541'

# getpass
# Substitui o input ao ler passwords do terminal.

password = getpass.getpass()
# Password: <invisible>
