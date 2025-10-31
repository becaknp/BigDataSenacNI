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