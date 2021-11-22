from random import *
from misc_config import *

print(terminal_start_message)

slot_list = ("Kertas, Batu, Gunting")
print("Slot: "+slot_list)
print("───────────────")

var_list = ["Kertas", "Batu", "Gunting"]

result = choice(var_list)

userinput = input("Kamu: ").lower()
enemy = ("Musuh: ")

if userinput == "kertas":
    if result == "Kertas":
        print(enemy+result)
        print("Seri")
    elif result == "Batu":
        print(enemy+result)
        print("Menang")
    elif result == "Gunting":
        print(enemy+result)
        print("Kalah")

if userinput == "batu":
    if result == "Kertas":
        print(enemy+result)
        print("Kalah")
    elif result == "Batu":
        print(enemy+result)
        print("Seri")
    elif result == "Gunting":
        print(enemy+result)
        print("Menang")

if userinput == "gunting":
    if result == "Kertas":
        print(enemy+result)
        print("Menang")
    elif result == "Batu":
        print(enemy+result)
        print("Kalah")
    elif result == "Gunting":
        print(enemy+result)
        print("Seri")

print(terminal_end_message)