#!/usr/bin/env python3
"""
Faça um programa que imprime os números pares de 1 a 200

ex
`python3 numeros.py`
2
4
6
...
"""
__version__ = "0.0.1"

for num in range(1,201):
    if num % 2 == 0:
        print(num)
