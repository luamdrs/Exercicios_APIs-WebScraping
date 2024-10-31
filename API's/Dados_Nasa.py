import requests

url = 'https://api.nasa.gov/planetary/apod'
api_key = 'TlZB0BVeSWWQUZfJV4NrMDX998xinOBIy2L1phOg'

parametros = {
    'api_key': api_key,
    'date': '2024-10-30'
}

response = requests.get(url, params=parametros)

if response.status_code == 200:
    dados = response.json()

    print(f'Título: {dados['title']}')
    print(f'Data: {dados['date']}')
    print(f'Descrição: {dados['explanation']}')
    print(f'URL da imagem: {dados['url']}')
else:
    print('Erro na requisição:', response.status_code)