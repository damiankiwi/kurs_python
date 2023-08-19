import site

site_packages_path = site.getsitepackages()

print("Lokalizacje pakietów Pythona:")
for path in site_packages_path:
    print(path)
