#2

from datetime import date

print("--- Cadastro de Candidatos ---")
ano_atual = date.today().year

for i in range(12):
    print(f"\nCandidato {i + 1} de 12")
    try:
        ano_nasc = int(input("Ano de nascimento: "))
        idade = ano_atual - ano_nasc

        if idade < 18:
            print(f"Idade: {idade} anos → Menor de idade. Não pode participar.")
            continue  # pula pro próximo candidato

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        print(f"Cadastro concluído: {nome}, {idade} anos.")

    except ValueError:
        print("Entrada inválida.")
