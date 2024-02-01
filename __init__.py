from os import system

try:
    import colorama
except ModuleNotFoundError:
    system("pip install colorama")

try:
    import inquirer
except ModuleNotFoundError:
    system("pip install inquirer")