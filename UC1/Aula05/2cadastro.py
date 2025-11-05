# ===========================
# 2. Cadastro de Candidatos
# ===========================
print("\n=== Cadastro de Candidatos ===")
ano_atual = 2025  # Pode usar datetime.now().year se preferir (aí precisa fazer import datetime)


# from datetime import datetime
# ano_atual = datetime.now().year


for i in range(1, 13):  # 12 candidatos
    print(f"\nCandidato {i}:")
    try:
        ano_nasc = int(input("Digite o ano de nascimento: "))
        idade = ano_atual - ano_nasc

        if idade < 18:
            print("Não pode participar (menor de 18 anos).")
            continue  # pula para o próximo candidato
        else:
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            print(f"Cadastro concluído para candidato {i}.")
    except ValueError:
        print("Ano inválido! Digite apenas números para o ano de nascimento.")