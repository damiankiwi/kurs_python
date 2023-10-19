import platform

architektura = platform.architecture()[0]

if architektura == '32bit':
    print("Python działa w trybie 32-bitowym.")
elif architektura == '64bit':
    print("Python działa w trybie 64-bitowym.")
else:
    print("Nie można określić trybu bitowego Pythona.")
