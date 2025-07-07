import requests

def consultar_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()

            if "erro" in dados:
                print("CEP não encontrado.\n")
            else:
                logradouro = dados.get("logradouro", "Não informado")
                bairro = dados.get("bairro", "Não informado")
                cidade = dados.get("localidade", "Não informado")
                estado = dados.get("uf", "Não informado")

                print("\n--- Endereço Encontrado ---")
                print(f"Logradouro: {logradouro}")
                print(f"Bairro    : {bairro}")
                print(f"Cidade    : {cidade}")
                print(f"Estado    : {estado}")
                print("----------------------------\n")
        else:
            print("Erro ao acessar a API.\n")

    except Exception as e:
        print(f"Ocorreu um erro: {e}\n")

while True:
    cep = input("Digite o CEP (apenas números) ou 'sair' para encerrar: ")

    if cep.lower() == 'sair':
        print("Programa encerrado.")
        break

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido! Digite 8 números.\n")
        continue

    consultar_cep(cep)
