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

n_lampadas_float = potencia_necessaria/potencia
n_lampadas_int = int(n_lampadas_float)

if n_lampadas_float > n_lampadas_int:
    n_lampadas_final = n_lampadas_int + 1
else:
    n_lampadas_final = n_lampadas_int

print(f'Resultado:\n Área: {area:.2f} m²')
print(f'Lâmapadas necessarios: {n_lampadas_final}\n')

#Professor

print("--- 1. CÁLCULO DE LÂMPADAS ---")
try:
    potencia_lampada = float(input("Potência de uma lâmpada (W): "))
    largura = float(input("Largura do cômodo (m): "))
    comprimento = float(input("Comprimento do cômodo (m): "))
    
    area = largura * comprimento
    potencia_total_necessaria = area * 3 
    
    num_lampadas_float = potencia_total_necessaria / potencia_lampada
    num_lampadas_inteiro = int(num_lampadas_float)
    
    if num_lampadas_float > num_lampadas_inteiro:
        num_lampadas_final = num_lampadas_inteiro + 1
    else:
        num_lampadas_final = num_lampadas_inteiro
        
    print(f"Resultado:\n  Área: {area:.2f} m²")
    print(f"  Lâmpadas necessárias: {num_lampadas_final}\n")
    
except ValueError:
    print("ERRO: Por favor, digite apenas números válidos.")
except ZeroDivisionError:
    print("ERRO: A potência da lâmpada não pode ser zero.")




