#!/usr/bin/env python

"""Imprime a tabuada de 1 à N.

---Tabuada do 1---
    1 * 1 = 1
    2 * 1 = 2
    3 * 1 = 3
...
###################
---Tabuada do 2---
    2 * 2 = 4
    4 * 2 = 8
...
###################
"""
__version__ = "0.1.1"
__author__ = "Davi Carmo"

N = 10
numeros = list(range(1,(N + 1)))

for n1 in numeros:
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()

    for n2 in numeros:
        resultado = n1 * n2
        print("{:^20}".format(f"{n1} * {n2} = {resultado}"))

    print("#" * 20 + "\n")
