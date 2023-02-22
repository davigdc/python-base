#!/usr/bin/env python3
"""
Alarme de temperatura

"""
__version__ = "0.0.2"

import sys

info = {
    "temperatura": None,
    "umidade": None,
}

# while True:
#     # condicao de parada
#     # o dicionario esta completamente preenchido
#     info_size = len(info.values())
#     filled_size = len([value for value in info.values() if value is not None])
#     if info_size == filled_size:
#         break

for key in info.keys():
    try:
        info[key] = float(input(f"Qual a {key} atual? ").strip())
    except ValueError as e:
        print(f"Valor inválido, digite um número.\n(`{e}`)")
        sys.exit(1)

temp, umidade = info.values()

if temp > 45:
    print("⚠️ ALERTA!!! Perigo calor extremo. 🥵")

elif temp != 0 and temp * 3 >= umidade:
    print("⚠️ ALERTA!!! Perigo de calor umido. 🥵")

elif temp > 10 and temp < 30:
    print("Normal. 🙂")

elif temp >= 0 and temp <= 10:
    print("Frio. ❄️")

elif temp < 0:
    print("⚠️ ALERTA!!! Frio extremo. 🥶")
