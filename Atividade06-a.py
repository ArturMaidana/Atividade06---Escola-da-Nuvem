import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

while True:
    try:
        tamanho = int(input("Digite a quantidade de caracteres da senha (ou 0 para sair): "))

        if tamanho == 0:
            print("Programa encerrado.")
            break

        if tamanho < 4:
            print("Para segurança, a senha deve ter pelo menos 4 caracteres.")
            continue

        senha_gerada = gerar_senha(tamanho)
        print(f"\nSenha gerada: {senha_gerada}\n")

    except ValueError:
        print("Entrada inválida! Digite um número inteiro.\n")
