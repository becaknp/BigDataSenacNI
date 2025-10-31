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