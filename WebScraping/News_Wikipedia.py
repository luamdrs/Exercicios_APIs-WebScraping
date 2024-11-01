import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    new_titles = soup.select('#mp-itn b a')

    if new_titles:
        print('Notícias da Wikipedia:')
        for title in new_titles:
            print(title.get_text())
    else:
        print('Nenhum título encontrado.')
else:
    print('Erro de requisição:', response.status_code)