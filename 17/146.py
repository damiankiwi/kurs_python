import importlib.util

module_name = "math"

spec = importlib.util.find_spec(module_name)
if spec is not None:
    source_location = spec.origin
    print(f"Lokalizacja źródeł modułu {module_name}: {source_location}")
else:
    print(f"Moduł {module_name} nie istnieje.")