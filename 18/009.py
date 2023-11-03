import pkgutil

def get_installed_python_modules():
    modules = []
    for module in pkgutil.iter_modules():
        modules.append(module.name)
    return modules

if __name__ == "__main__":
    installed_modules = get_installed_python_modules()
    print("Zainstalowane moduły Pythona:")
    for module in installed_modules:
        print(module)
