#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read tech
...
...

"""
__version__ = "0.1.0"

import os, sys
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
cmds = ("read", "new")

if not arguments:
    print("Invalid usage.")
    print(f"Possible subcommands: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    
if arguments[0] == "read":
    # leitura das notas
    try:
        _file = open(filepath)
    except FileNotFoundError as e:
        print(str(e))
        sys.exit(1)

    for line in _file:
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 50)

if arguments[0] == "new":
    try:
        title = arguments[1]
    except IndexError as e:
        print(f"[ERROR] {str(e)}")
        print("You need to pass the title of the note. eg.: `notes.py new title`")
        sys.exit(1)

    text = [
        f"{title}",
        input("Tag: ").strip(),
        input("Text: ").strip(),
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
