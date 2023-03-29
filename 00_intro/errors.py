#!/usr/bin/env python3
import logging
import time

log = logging.Logger("errors")

#  EAFP - Easy to ask Forgiveness than permission


def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""
    for attempt in range(1, retry+1):
        try:
            return open("names.txt").readlines()
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
            time.sleep(2)
        else:
            print("Sucesso!!!")
        finally:
            print("Execute isso sempre!")
    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)
