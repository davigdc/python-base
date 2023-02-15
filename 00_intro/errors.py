#!/usr/bin/env python3
import os, sys

#  EAFP - Easy to ask Forgiveness than permission

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(str(e))
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[ERROR] Missing name in the list")
