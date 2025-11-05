# '''5. Média do Aluno com Optativa:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0
# Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
# resultado final.
# ''' if e else

#Objetivo: calcular a média e o resultado (aprovado, reprovado, recuperação).

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
opt = float(input("Nota optativa (-1 se não fez): "))

if opt != -1:
    menor = min(n1, n2)
    if menor == n1:
        n1 = opt
    else:
        n2 = opt

media = (n1 + n2) / 2

if media >= 6:
    print(f"Média {media:.1f} → Aprovado")
elif media < 3:
    print(f"Média {media:.1f} → Reprovado")
else:
    print(f"Média {media:.1f} → Recuperação")

#Professor

print("--- 5. MÉDIA DO ALUNO ---")
try:
    n1 = float(input("Nota N1: "))
    n2 = float(input("Nota N2: "))
    optativa = float(input("Nota Optativa (-1 se não fez): "))

    nota_final_1 = n1
    nota_final_2 = n2

    # PONTO DE DECISÃO 1: Substituição (IF ANINHADO)
    if optativa != -1:
        # Se N1 é a menor nota (ou igual), substitui N1
        if nota_final_1 <= nota_final_2:
            nota_final_1 = optativa
        else: # Se N2 é menor
            nota_final_2 = optativa
            
    media = (nota_final_1 + nota_final_2) / 2.0

    # PONTO DE DECISÃO 2: Situação Final (IF/ELIF/ELSE)
    if media >= 6.0:
        situacao = "APROVADO"
    elif media < 3.0:
        situacao = "REPROVADO"
    else:
        situacao = "EM EXAME (Recuperação)"

    print(f"Resultado:\n  Média Final: {media:.1f}")
    print(f"  Situação: {situacao}\n")

except ValueError:
    print("ERRO: Digite apenas números válidos.")
