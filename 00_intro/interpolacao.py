#!/usr/bin/env python
"""Imprime a mensagem de um e-mail

Para abrir um servidor local e ver as mensagens chegando, 
execute em um terminar:
$ python -m smtpd -c DebuggingServer -n localhost:8025

Depois execute este arquivo.
"""
__version__ = "0.2.0"

import os
import sys
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if len(arguments) != 2:
    print("Informe dois nomes de arquivos como parâmetro (emails, template).")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host="localhost", port=8025) as server:
    for line in open(filepath):
        name, email = line.split(",")
        text = (
            open(templatepath).read()
            % {
                "nome": name,
                "produto": "caneta",
                "texto": "Escrever muito bem",
                "link": "http://canetaslegais.com",
                "quantidade": 1,
                "preco": 50.5,
            }
        )

        from_ = "davigdc10@gmail.com"
        to = ", ".join([email])

        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())
