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
__version__ = "0.1.0"

import sys, os
from datetime import datetime

arguments = sys.argv[1:]

if not arguments:
    operation = input("Operation: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("Invalid number of arguments.")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments
valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Invalid Operation")
    print(valid_operations)
    sys.exit(1)

validated_nums = []

for num in nums:
    # TODO: Repetição while
    if not num.replace(".", "").isdigit():
        print(f"Invalid argument `{num}`")
        sys.exit(1)
    elif "." in num:
        num = float(num)
    else:
        num = int(num)
    
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueError as e:
    print(f"[ERROR] {str(e)}")
    sys.exit(1)

# TODO: Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
else:
    try:
        result = n1 / n2
    except ZeroDivisionError as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
except PermissionError as e:
    # TODO: logging
    print(str(e))
    sys.exit(1)

print(f"O resultado é: {result}")
