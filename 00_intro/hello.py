#!/usr/bin/env python3

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

    ./hello.py 
    ./hello.py --lang=pt_BR
    ./hello.py --lang=pt_BR --count=2

"""
__version__ = "0.1.3"
__author__ = "Davi Carmo"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split('=')
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")[:5]
    else:
        current_language = input("Choose a language: ")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Cia, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!",
}

print(
    msg[current_language] * int(arguments["count"])
)