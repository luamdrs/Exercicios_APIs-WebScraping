import requests

def obter_taxa_cambio(moeda_origem, moeda_destino):
    api_key = '5533e65c43279fdf6c5f7e4a'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{moeda_origem}/{moeda_destino}'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        taxa = dados['conversion_rate']
        print(f'Taxa de câmbio de {moeda_origem} para {moeda_destino}: {taxa}')
    else:
        print('Erro na requisição:', resposta.status_code)

moeda_origem = input('Digite a moeda de origem [ex: USD]: ').upper()
moeda_destino = input('Digite a moeda de destino [ex: USD]: ').upper()

obter_taxa_cambio(moeda_origem, moeda_destino)