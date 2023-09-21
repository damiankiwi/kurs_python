import traceback

def funkcja_a():
    funkcja_b()

def funkcja_b():
    funkcja_c()

def funkcja_c():
    stos_wywolan = traceback.format_stack()
    for wywolanie in stos_wywolan:
        print(wywolanie)

funkcja_a()
