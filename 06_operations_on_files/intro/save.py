items = ['latarka', 'woda', 'namiot', 'źdźbło', 'gąbka']

# with open('example.txt', 'w') as fopen:
with open('example.txt', 'w', encoding="utf-8") as fopen:
    print(fopen)
    fopen.write('\n'.join(items))