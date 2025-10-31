'''Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
3m² existe um bocal para uma lâmpada.
'''

#Objetivo: calcular quantas lâmpadas são necessárias para iluminar um cômodo.

potencia = float(input('Digite a potencia da lâmpada: '))
largura = float(input('Qual a largura em metros?: '))
comprimento = float(input('Qual o comprimento em metros?: '))
area = largura*comprimento
potencia_necessaria = area*3
n_lampadas = area/3

if potencia <= 0:
    print('Potência inválida. Digite um valor maior que zero.')
else:
    print(f'Área do cômodo: {area} m²')
    print(f'Potência necessária para iluminar o cômodo: {potencia_necessaria} watts')
    print(f'Número de lâmpadas necessárias: {n_lampadas:.0f}')





