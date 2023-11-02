import requests
from bs4 import BeautifulSoup


def pobierz_najwazniejsze_wiadomosci():
    url = 'https://news.google.com/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        naglowki = soup.find_all('h3')

        print("Najważniejsze wiadomości z Google News:")
        for index, naglowek in enumerate(naglowki, start=1):
            tytul = naglowek.get_text()
            print(f"{index}. {tytul}")
    else:
        print("Nie udało się pobrać wiadomości.")


if __name__ == "__main__":
    pobierz_najwazniejsze_wiadomosci()
