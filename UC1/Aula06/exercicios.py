# Desafios (ugprade):
### Média Escolar para 5 Estudantes ###
# Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().

# Lista para armazenar os resultados
# resultados = []

# print("SISTEMA DE MÉDIA ESCOLAR")

# for i in range(1, 6):  # 1 a 5 (5 alunos)
#     print(f"\n--- Aluno {i} ---")
    
#     # Validação das notas
#     while True:
#         try:
#             nota1 = float(input("Digite a primeira nota (0-10): "))
#             if nota1 < 0 or nota1 > 10:
#                 print("Nota deve estar entre 0 e 10!")
#                 continue
#             break
#         except ValueError:
#             print("Digite apenas números!")
    
#     while True:
#         try:
#             nota2 = float(input("Digite a segunda nota (0-10): "))
#             if nota2 < 0 or nota2 > 10:
#                 print("Nota deve estar entre 0 e 10!")
#                 continue
#             break
#         except ValueError:
#             print("Digite apenas números!")
    
#     # Cálculo da média
#     media = (nota1 + nota2) / 2
    
#     # Decisão baseada na média
#     if media >= 7:
#         situacao = "APROVADO"
#     elif media >= 5:
#         situacao = "RECUPERAÇÃO"
#     else:
#         situacao = "REPROVADO"
    
#     # Adiciona à lista
#     resultado_str = f"Aluno {i} - Média: {media:.1f} - {situacao}"
#     resultados.append(resultado_str)

# # Exibe todos os resultados
# print("\n" + "="*50)
# print("RESULTADOS FINAIS:")
# print("="*50)

# for i in range(len(resultados)):
#     print(resultados[i])

# print(f"\n Total de alunos processados: {len(resultados)}")


#Professor
# resultadofinal=[]

# for estudante in range (1,6):
#     try:
#         n1 = float(input("Nota N1: "))
#         n2 = float(input("Nota N2: "))
#         optativa = float(input("Nota Optativa (-1 se não fez): "))

#         nota_final_1 = n1
#         nota_final_2 = n2

#         # PONTO DE DECISÃO 1: Substituição (IF ANINHADO)
#         if optativa != -1:
#             # Se N1 é a menor nota (ou igual), substitui N1
#             if nota_final_1 <= nota_final_2:
#                 nota_final_1 = optativa
#             else: # Se N2 é menor
#                 nota_final_2 = optativa
                
#         media = (nota_final_1 + nota_final_2) / 2.0

#         # PONTO DE DECISÃO 2: Situação Final (IF/ELIF/ELSE)
#         if media >= 6.0:
#             situacao = "APROVADO"
#         elif media < 3.0:
#             situacao = "REPROVADO"
#         else:
#             situacao = "RECUPERAÇÃO"
        
#         resultadofinal.append(situacao)

#         print(f"Resultado:\n  Média Final: {media:.1f}")
#         print(f"  Situação: {situacao}\n")
#         print(f'Lista Final:[{resultadofinal}')

#     except ValueError:
#         print("ERRO: Digite apenas números válidos.")


### Cadastro Seletivo de Candidatos ###
# Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
# Adicione este Dicionário à lista: candidatos_validos.append(candidato)

# Lista para armazenar candidatos válidos
# candidatos_validos = []
# candidatos_rejeitados = 0

# print("=== CADASTRO SELETIVO DE CANDIDATOS ===")

# for i in range(1, 6):  # 1 a 5 (5 candidatos)
#     print(f"\n--- Candidato {i} ---")
    
#     # Coleta e validação do nome
#     while True:
#         nome = input("Digite o nome completo: ").strip()
#         if nome == "":
#             print(" Nome não pode estar vazio!")
#         else:
#             break
    
#     # Coleta e validação da idade
#     while True:
#         try:
#             idade = int(input("Digite a idade: "))
#             if idade < 0 or idade > 120:
#                 print(" Idade deve ser entre 0 e 120 anos!")
#                 continue
#             break
#         except ValueError:
#             print(" Digite apenas números para a idade!")
    
#     # Verificação da elegibilidade
#     if idade < 18:
#         print(f" {nome} foi REJEITADO - Menor de 18 anos")
#         candidatos_rejeitados += 1
#         continue  # Pula para o próximo candidato
    
#     # Coleta dos demais dados (apenas se for maior de idade)
#     email = input("Digite o e-mail: ").strip()
#     telefone = input("Digite o telefone: ").strip()
    
#     # Cria dicionário do candidato
#     candidato = {
#         'nome': nome,
#         'idade': idade,
#         'email': email,
#         'telefone': telefone
#     }
    
#     # Adiciona à lista de válidos
#     candidatos_validos.append(candidato)
#     print(f" {nome} foi ACEITO no cadastro")

# # Relatório Final
# print("\n" + "="*60)
# print("RELATÓRIO FINAL DO PROCESSO SELETIVO")
# print("="*60)

# print(f" Candidatos válidos: {len(candidatos_validos)}")
# print(f" Candidatos rejeitados: {candidatos_rejeitados}")
# print(f" Total processados: {len(candidatos_validos) + candidatos_rejeitados}")

# if len(candidatos_validos) > 0:
#     print("\n LISTA DE CANDIDATOS ACEITOS:")
#     print("-" * 40)
#     for i in range(len(candidatos_validos)):
#         cand = candidatos_validos[i]
#         print(f"{i+1}. {cand['nome']} | {cand['idade']} anos | {cand['email']}")
# else:
#     print("\nℹ Nenhum candidato atendeu aos requisitos de idade.")

#Professor

listagem_candidatos=[]
contador_candidatos=3
for candidato in range(contador_candidatos):
    try:
        print("Bem-vindo(a) ao nosso processo de candidaturas! Vamos começar.")
        ano_nascimento=int(input('Por favor informe o ano de nascimento: '))
        ano_atual=2025
        idade=ano_atual-ano_nascimento

        if idade <18:
            print('Você parece ter menos de 18 anos. Não poderá participar da candidatura')
        elif idade >= 18:
            nome=(input('Nome: '))
            telefone=input('Telefone: ')
            email=input('email: ')
            contador_candidatos-=1
            candidato={
            'nome': nome,
            'telefone': telefone,
            'email': email,
        }
            print('-'*90)
            print("Obrigado por se inscrever! Dados da sua candidatura:\n",telefone,"\n",email, ".")
            print('-'*90)
        else:
            print('Favor informar um ano de nascimento válido.')
        
        listagem_candidatos.append(candidato)
       
    except ValueError:
        print("ERRO: Informe dados válidos.")
    except SyntaxError:
        print("ERRO: Informe dados válidos.")

print(listagem_candidatos)


#def calculadora(variavel):
                # parametro
#função