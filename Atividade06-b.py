import requests

def gerar_perfil():
    try:
        resposta = requests.get("https://randomuser.me/api/")
        if resposta.status_code == 200:
            dados = resposta.json()
            usuario = dados['results'][0]

            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']

            print("\n--- Perfil Gerado ---")
            print(f"Nome : {nome}")
            print(f"Email: {email}")
            print(f"País : {pais}")
            print("---------------------\n")
        else:
            print("Erro ao acessar a API.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

while True:
    opcao = input("Deseja gerar um perfil aleatório? (s/n): ").lower()
    if opcao == 's':
        gerar_perfil()
    elif opcao == 'n':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Digite 's' ou 'n'.")
