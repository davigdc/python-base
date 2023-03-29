#!/usr/bin/env python3
"""
Alarme de temperatura

"""
__version__ = "0.0.3"

import logging

log = logging.Logger("alert")

# TODO: Mover para módulo de utilidades


def is_completely_filled(dict_of_inputs):
    """Returns a boolean teling if a dict is completely filled."""
    info_size = len(info.values())
    filled_size = len(
        [value for value in info.values() if value is not None]
    )

    return info_size == filled_size


def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = float(input(f"Qual a {key} atual? ").strip())
        except ValueError as e:
            log.error("%s inválida, digite números", key.title())
            break

# Programa principal


info = {
    "temperatura": None,
    "umidade": None,
}

while not is_completely_filled(info):
    read_inputs_for_dict(info)

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
