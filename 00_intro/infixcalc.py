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

import sys
import os
import logging
from datetime import datetime

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger(os.getenv("USER", "anonymous"), log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = sys.argv[1:]

valid_operations = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")


while True:

    if not arguments:
        operation = input("Operation: ")
        n1 = input("n1: ")
        n2 = input("n2: ")
        arguments = [operation, n1, n2]

    elif len(arguments) != 3:
        log.error("Invalid number of arguments. Try like: `sum 5 5`")
        sys.exit(1)

    operation, *nums = arguments

    if operation not in valid_operations:
        log.error("Invalid Operation: `%s`", operation)
        sys.exit(1)

    validated_nums = []
    for num in nums:
        if not num.replace(".", "").isdigit():
            log.error("Invalid argument: `%s`", num)
            sys.exit(1)
        elif "." in num:
            num = float(num)
        else:
            num = int(num)
        validated_nums.append(num)

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        log.error(str(e))
        sys.exit(1)

    try:
        result = valid_operations[operation](n1, n2)
        print(f"O resultado é: {result}")
    except ZeroDivisionError as e:
        log.error("Division per zero not possible.")
        sys.exit(1)

    try:
        with open(filepath, "a") as file_:
            file_.write(
                f"{timestamp} - {user} - {operation},{n1},{n2} = {result}\n")
    except PermissionError as e:
        log.error(str(e))
        sys.exit(1)

    arguments = None

    if input("Perssione enter para continuar ou qualquer tecla para sair."):
        break
