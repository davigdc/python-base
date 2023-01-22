#!/usr/bin/env python

"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
---------------
Tabuada do 2
2
4
6
...
---------------
"""
__version__ = "0.0.1"
__author__ = "Davi Carmo"

numeros = list(range(1,11))

for numero in numeros:
    print(f"Tabuada do: {numero}")
    for x in numeros:
        print(f"{numero} * {x} = {numero * x}")
    print("-" * 15)
