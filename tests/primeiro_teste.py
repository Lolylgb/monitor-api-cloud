import requests

url = "https://api.github.com"

try:
    resposta = requests.get(url, timeout=10)

    print("Código HTTP:", resposta.status_code)

    if resposta.ok:
        print("A API está respondendo corretamente.")
    else:
        print("A API respondeu com um erro HTTP.")

except requests.RequestException as erro:
    print("Não foi possível consultar a API.")
    print("Detalhes:", erro)