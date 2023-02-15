#!/usr/bin/env python3
import os, sys

# LBYL - Look Before You Leap

if os.path.exists("names.txt"):
    print("O arqvuivo existe")
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("[ERROR] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[ERROR] Missing name in the list")
