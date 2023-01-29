#!/usr/bin/env python3

"""Calculadora infix.

Funcionamento:
[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

"""
__version__ = "0.0.1"

from sys import argv, exit

# Operações aceitas
operacoes = {"sum", "sub", "mul", "div"}

# Valida se o primeiro parâmetro é uma operação possivel válida.
def valida_operacao(opr):
    if opr not in operacoes:
        print(f"Operação inválida (`{opr}`).")
        exit()

    return opr

# Valida se segundo e terceiro parâmetros são números e retorna como float
def valida_numeros(numeros):
    for i in numeros:
        try:
            float(i)
        except:
            print(f"Parâmetro inválido (`{i}`), segundo e terceiro parâmentro devem ser números.")
            exit()
    
    return [float(numeros[0]), float(numeros[1])]

def calculo(opr, n1, n2):
    if opr == "sum":
        return n1 + n2
    elif opr == "sub":
        return n1 - n2
    elif opr == "mul":
        return n1 * n2
    else:
        if n2 == 0:
            print("Impossível divisão por 0.")
            exit()
        return n1 / n2

# Variaveis de controle
operacao = ""
n1 = ""
n2 = ""

# Caso usuário digite por exemplo "infixcalc.py sum 5 2".
if len(argv) == 4:
    operacao = valida_operacao(argv[1])
    n1, n2 = valida_numeros([argv[2], argv[3]])

# Caso usuário digite "infixcalc.py"
elif len(argv) == 1:
    print("Operação:")
    operacao = input()
    valida_operacao(operacao)

    print("n1: ")
    n1 = input()
    print("n2: ")
    n2 = input()
    n1, n2 = valida_numeros([n1,n2])

# Caso usuário passe número de argumentos inválido
else:
    print("Número de parametros errado.")
    exit()

resultado = calculo(operacao, n1, n2)

print(resultado)
