#!/usr/bin/env python3

"""Exibe relatorio de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam
cada umas das atividades.
"""
__version__ = "0.1.2"

salas = {
    "sala1": ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "ingles": ["Erick", "Maia", "Joana", "Carlos", "Antonio"],
    "musica": ["Erick", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

# Listar alunos em cada atividade por sala
for atividade, alunos_atividade in atividades.items():
    print(f"Alunos da atividade {atividade.title()} por sala:")

    for sala, alunos_sala in salas.items():
        # Realiza a intersecao entre os conjuntos
        alunos = set(alunos_sala) & set(alunos_atividade)
        print(f"{sala.title()}: {alunos}")

    print(f"\n{'-' * 40}\n")
