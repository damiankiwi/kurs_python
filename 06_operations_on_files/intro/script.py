handler = open("pan_tadzio.txt")
print(handler.readline())
handler.close()

print('-------------------')
with open("pan_tadzio.txt", encoding ="utf-8") as fo:
    # print(fo)
    print(fo.readline())

filename = 'pan_tadzio.txt'
with open(filename, 'r') as f:
  content = f.read()
  print()

  # handler = open("pan_tadzio.txt")
  # print(handler.readline())
  # handler.close()
  #
  # print('-----------------')
  #
  # with open("pan_tadzio.txt") as fo:
  #     print(fo.readline())
  #     print(fo)