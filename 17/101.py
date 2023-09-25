import urllib.request

url = "https://www.example.com"

try:
    with urllib.request.urlopen(url) as response:
        zawartosc = response.read().decode('utf-8')

    print(zawartosc)

except Exception as e:
    print("Wystąpił błąd:", str(e))
