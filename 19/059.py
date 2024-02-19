def is_valid_filename(filename):
    valid_extensions = ['.txt', '.exe', '.jpg', '.png', '.dll']

    if '.' not in filename:
        return 'No'

    name, extension = filename.rsplit('.', 1)
    if extension.lower() in valid_extensions and name.isdigit() and len(name) <= 3:
        return 'Yes'
    else:
        return 'No'

filenames1 = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
output1 = [is_valid_filename(filename) for filename in filenames1]
print(f"Input:\n{filenames1}\nOutput:\n{output1}")

filenames2 = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']
output2 = [is_valid_filename(filename) for filename in filenames2]
print(f"\nInput:\n{filenames2}\nOutput:\n{output2}")