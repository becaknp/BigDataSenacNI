# '''
# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²'''

#Objetivo: descobrir quantas caixas de azulejos são necessárias para cobrir as paredes de uma cozinha.

comprimento = float(input('Digite o comprimento: '))
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

if comprimento <= 0 or largura <= 0 or altura <= 0:
    print('Valores inválidos. Digite valores maiores que zero.')
else:
    area = 2*altura*(comprimento + largura)
    caixa = area/1.5
    print(f'Serão necessárias {caixa:.0f} caixas de azulejos.')


#Professor

print("--- 2. CAIXAS DE AZULEJOS ---")
try:
    AREA_CAIXA = 1.5
    
    comprimento = float(input("Comprimento da cozinha (m): "))
    largura = float(input("Largura da cozinha (m): "))
    altura = float(input("Altura da cozinha (m): "))
    
    area_total_paredes = (2 * comprimento * altura) + (2 * largura * altura)
    num_caixas_float = area_total_paredes / AREA_CAIXA
    
    num_caixas_inteiro = int(num_caixas_float)
    
    # Lógica de Arredondamento (IF/ELSE)
    if num_caixas_float > num_caixas_inteiro:
        num_caixas_final = num_caixas_inteiro + 1
    else:
        num_caixas_final = num_caixas_inteiro
        
    print(f"Resultado:\n  Área total: {area_total_paredes:.2f} m²")
    print(f"  Caixas necessárias: {num_caixas_final}\n")

except ValueError:
    print("ERRO: Por favor, digite apenas números válidos.")
