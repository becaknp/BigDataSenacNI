#### Desafio 2: Cálculo de Média e Status do Estudante ####

# Dadas as 4 notas de um estudante, calcule sua média e, com base nela, emita a mensagem de status correspondente:
# 1. Aprovado: Média estritamente maior que 7.
# 2. Recuperação: Média entre 5 (inclusive) e 7 (inclusive).
# 3. Reprovação: Média estritamente abaixo de 5.

n1=float(input('Primeira Nota:'))
n2=float(input('Segunda Nota:'))
n3=float(input('Terceira Nota:'))
n4=float(input('Quarta Nota:'))

media=(n1+n2+n3+n4)/4
corte=7

if media > corte:
    print('Aprovado')
elif 5 <= media <= 7:
    print('Recuperação')
elif media < 5:
    print ('Reprovado')
else:
    print('Informe um valor adequado para as notas')

