def konwertuj_do_float(lista):
    return [float(element) for element in lista]

original_list = ['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', '0.54', '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']
print("Oryginalna lista:", original_list)
print("Lista liczb zmiennoprzecinkowych:", konwertuj_do_float(original_list))