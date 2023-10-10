import types

sample_object = "To jest przykład obiektu"


module_object = types.ModuleType('my_module', 'To jest przykład modułu')
module_object.__dict__.update(globals())

print("Obiekt modułu dla obiektu:", sample_object)
print("Nazwa modułu:", module_object.__name__)
print("Opis modułu:", module_object.__doc__)