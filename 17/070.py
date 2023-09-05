import os

def sort_files_by_date(folder_path):
    files = os.listdir(folder_path)

    sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    return sorted_files

folder_path = input("Podaj ścieżkę do folderu: ")

try:
    sorted_files = sort_files_by_date(folder_path)
    print("Posortowane pliki według daty modyfikacji:")
    for file in sorted_files:
        print(file)
except FileNotFoundError:
    print("Podany folder nie istnieje.")
