import platform

os_name = platform.system()
os_platform = platform.platform()
os_release = platform.release()

print(f"Nazwa systemu operacyjnego: {os_name}")
print(f"Platforma: {os_platform}")
print(f"Wersja systemu operacyjnego: {os_release}")
