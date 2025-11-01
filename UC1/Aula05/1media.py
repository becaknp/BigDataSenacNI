print("--- Cálculo de Média Escolar ---")

for i in range(10):
    print(f"\nAluno {i + 1} de 10")
    try:
        n1 = float(input("Digite a 1ª nota: "))
        n2 = float(input("Digite a 2ª nota: "))
        media = (n1 + n2) / 2

        if media >= 7:
            status = "Aprovado"
        elif media >= 5:
            status = "Recuperação"
        else:
            status = "Reprovado"

        print(f"Média = {media:.1f} → {status}")

    except ValueError:
        print("Entrada inválida. Tente novamente.")



