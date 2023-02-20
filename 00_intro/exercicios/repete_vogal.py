#!/usr/bin/env python3
"""
Repete Vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e
imprime cada uma das palavras com suas vogais duplicadas.

ex
./repete_vogal.py
Digite uma palavra (ou presione enter para sair): Davi
Digite uma palavra (ou presione enter para sair): Carmo
Digite uma palavra (ou presione enter para sair): <enter>
Daavii
Caarmoo
"""
__version__ = "0.0.1"

words = []
vowels = ("a", "e", "i", "o", "u")

while True:
    word = input("Digite uma palavra (ou presione enter para sair): ").strip()

    if not word:
        break
    
    words.append(word)

for word in words:
    result = ''
    
    for letter in word:
        # TODO: Tratar acentuação usando função
        if letter.lower() in vowels:
            result += letter * 2
        else:
            result += letter
    
    print(result)
