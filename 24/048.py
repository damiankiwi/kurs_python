def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        for line in src:
            dest.write(line)

source_file = 'source.txt'
destination_file = 'destination.txt'

copy_file_contents(source_file, destination_file)

print(f"Contents of {source_file} copied to {destination_file} successfully.")
