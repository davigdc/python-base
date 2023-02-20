#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma lista do quartos disponíveis
para alugar e o preço de cada quarto, esta informação está disponível em um arquivo
de texto separado por virgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado e a 
quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas.

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12
Davi,4,5

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma mensagem
informando que já está resevado.

"""
__version__ = "0.0.1"

import sys, os

path = os.curdir
rooms_file = os.path.join(path, "quartos.txt")
booked_file = os.path.join(path, "reservas.txt")

try:
    with open(rooms_file) as _file:
        rooms_raw = _file.readlines()
    with open(booked_file) as _file:
        bookeds_raw = _file.readlines()
except FileNotFoundError as e:
    print(str(e))
    sys.exit(1)

rooms = []

for room_raw in rooms_raw:
    room = room_raw.replace("\n", "")
    try:
        id, name, price = room.split(",")
        room_parsed = {
            "id": int(id),
            "name": name,
            "price": float(price),
        }
    except ValueError as e:
        print(f"[ERROR] Arquivo com erro de formatação. `{str(e)}`")
        sys.exit(1)        

    rooms.append(room_parsed)

bookeds = []

for booked_raw in bookeds_raw:
    booked = booked_raw.replace("\n", "")
    try:
        name, id, booked_days = booked.split(",")
        booked_parsed = {
            "name": name,
            "id": int(id),
            "booked_days": int(booked_days),
        }
    except ValueError as e:
        print(f"[ERROR] Arquivo com erro de formatação. `{str(e)}`")
        sys.exit(1)        

    bookeds.append(booked_parsed)

# print(rooms, bookeds, sep="\n")

print("Quartos:\n")
for room in rooms:
    print(f"ID: {room['id']}\tNome: {room['name']}\tPreço: {room['price']}")
    print("-" * 50)

user = {}

try:
    user["user_name"] = input("\nQual seu nome? ")
    user["user_room"] = int(input("Qual o ID do quarto a ser reservado? "))
    user["user_days"] = int(input("Qual a quantidade de dias a serem reservados? "))
except ValueError as e:
    print(f"[ERROR] Entrada inválida. `{str(e)}`")
    sys.exit(1)

for booked in bookeds:
    if booked["id"] == user["user_room"]:
        print("\n⚠️ Não é possível reservar quarto, outra pessoa já o reservou. 😢")
        sys.exit()

try:
    with open(booked_file, "a") as _file:
        book = f"{user['user_name']},{user['user_room']},{user['user_days']}\n"
        _file.write(book)

except KeyError as e:
    print(str(e))
    sys.exit(1)

print("Reserva realizada com sucesso! 🏖️")