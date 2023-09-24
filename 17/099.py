import os

if os.name == 'posix':  # Unix/Linux/Mac
    os.system('clear')
elif os.name == 'nt':  # Windows
    os.system('cls')
