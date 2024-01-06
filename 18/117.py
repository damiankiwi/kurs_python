import requests

def pobierz_i_wyswietl_strone(url):
    response = requests.get(url)
    print(f"Status strony internetowej: {response}")
    if response.status_code == 200:
        print("\nKod HTML strony internetowej:")
        print(response.text)

url_strony = "https://www.example.com"
pobierz_i_wyswietl_strone(url_strony)