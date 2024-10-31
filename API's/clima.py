import requests

def obter_clima(cidade):
    key_api = '9d606fac9219b46aaa44a379d9d2f8b6'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key_api}&units=metric&lang=pt_br'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        descricao = dados['weather'][0]['description']

        print(f'Clima em {cidade.capitalize()}:')
        print(f'Temperatura: {temperatura:.0f}°C')
        print(f'Umidade: {umidade}%')
        print(f'Condição: {descricao.capitalize()}')
    else:
        print('Erro na requisição:', resposta.status_code)

cidade = input('Digite o nome da cidade para verificar o clima: ')
obter_clima(cidade)