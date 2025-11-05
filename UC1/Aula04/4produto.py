# '''
# 4. Código de Origem do Produto:
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região
# de sua procedência, conforme a tabela abaixo:
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser
# encarado como “Importado”''' match case

#Objetivo: identificar a região de origem do produto com base em um código numérico.

codigo = int(input("Digite o código de origem (inteiro, ex: 7,15 ou 90): "))

match codigo: #&& -> and e or ->|
    case 1:
        print("Sul")
    case 2:
        print("Norte")
    case 3:
        print("Leste")
    case 4:
        print("Oeste")
    case 5 | 6:
        print("Nordeste")
    case 7 | 8 |  9:
        print("Sudeste")
    case 10:
        print("Centro-Oeste")
    case 11:
        print("Noroeste")
    case _:
        print("Importado")


#Professor

# ESTRUTURA MATCH/CASE
# match codigo:
#         case 1:
#             procedencia = "Sul"
#         case 2:
#             procedencia = "Norte"
#         case 3:
#             procedencia = "Leste"
#         case 4:
#             procedencia = "Oeste"
#         case 5 | 6:
#             procedencia = "Nordeste"
#         # Faixa com Condição (Guard: 'if')
#         case n if 7 <= n <= 9:
#             procedencia = "Sudeste"
#         case 10:
#             procedencia = "Centro-Oeste"
#         case 11:
#             procedencia = "Nordeste"
#         # Caso Padrão (Default)
#         case _:
#             procedencia = "Importado"

#     print(f"Resultado:\n  Código {codigo} -> Procedência: {procedencia}\n")

# except ValueError:
#     print("ERRO: Digite um número inteiro válido.")
