#!/usr/bin/env python3
"""
Exemplos de envio de e-mail

Para abrir um servidor local e ver as mensagens chegando, 
execute em um terminar:
$ python -m smtpd -c DebuggingServer -n localhost:8025

Depois execute este arquivo.
"""
import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "davigdc10@gmail.com"
TO = ["davi.carmo@direcional.com.br",
      "davigoncalvesdocarmo@outlook.com", "202203943987@alunos.estacio.br"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Hello World</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {TO}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
