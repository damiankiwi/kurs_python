import io
def search_bytes_in_file(file_path, match_bytes):
  with io.open(file_path, mode='rb') as file:
    for line in file:
      if match_bytes in line:
        print(f"Match found in file {file_path}")
        return True
    else:
      return False

match = b'foobar'
result = search_bytes_in_file('fontawesome-webfont.bin', match)
if result:
  print("Match found")
else:
  print("No match")