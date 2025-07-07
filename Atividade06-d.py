import requests

def consultar_cotacao(moeda):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            chave = f"{moeda}BRL"

            if chave in dados:
                info = dados[chave]
                print(f"\n--- Cotação {moeda}/BRL ---")
                print(f"Valor atual : R${info['bid']}")
                print(f"Valor máximo: R${info['high']}")
                print(f"Valor mínimo: R${info['low']}")
                print(f"Atualizado em: {info['create_date']}")
                print("----------------------------\n")
            else:
                print("Moeda não encontrada.\n")
        else:
            print("Erro ao acessar a API.\n")

    except Exception as e:
        print(f"Ocorreu um erro: {e}\n")

while True:
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP) ou 'sair' para encerrar: ").upper()

    if moeda == 'SAIR':
        print("Programa encerrado.")
        break

    if not moeda.isalpha() or len(moeda) != 3:
        print("Código inválido! Digite 3 letras, como USD ou EUR.\n")
        continue

    consultar_cotacao(moeda)
