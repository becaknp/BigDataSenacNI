# '''
# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.
# '''

#Objetivo: calcular o consumo e o lucro diário do taxista.

ini = float(input("Odômetro inicial: "))
fim = float(input("Odômetro final: "))
litros = float(input("Litros gastos: "))
valor = float(input("Valor recebido (R$): "))

if fim < ini:
    print("Erro: odômetro final menor que o inicial.")
else:
    km = fim - ini
    media = km / litros
    gasto = litros * 6.15
    lucro = valor - gasto

    print(f"Média: {media:.2f} km/L")
    print(f"Lucro líquido: R${lucro:.2f}")

#Professor

print("--- 3. RENDIMENTO DO TAXISTA ---")
try:
    PRECO_COMBUSTIVEL = 6.15
    
    km_inicial = float(input("Odômetro inicial (km): "))
    km_final = float(input("Odômetro final (km): "))
    litros_gastos = float(input("Litros de combustível gastos: "))
    valor_recebido = float(input("Valor total recebido (R$): "))

    distancia_percorrida = km_final - km_inicial
    custo_combustivel = litros_gastos * PRECO_COMBUSTIVEL
    lucro_liquido = valor_recebido - custo_combustivel
    
    # PONTO DE DECISÃO: Prevenção de divisão por zero (IF/ELSE)
    if litros_gastos > 0:
        media_consumo = distancia_percorrida / litros_gastos
    else:
        media_consumo = 0.0
        
    print(f"Resultado:\n  Média de Consumo: {media_consumo:.2f} km/L")
    print(f"  Lucro Líquido: R$ {lucro_liquido:.2f}\n")

except ValueError:
    print("ERRO: Por favor, digite apenas números válidos.")
