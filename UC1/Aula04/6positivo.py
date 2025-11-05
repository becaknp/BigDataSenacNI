# '''6. Positivo ou Negativo:
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
# valor zero como positivo.
# ''' 0 = positivo

#Objetivo: verificar se o número é positivo ou negativo.

valor = float(input("Digite um valor: "))

if valor >= 0:
    print("Esse valor é positivo")
else:
    print("Esse valor é negativo")

#professor

print("--- 6. POSITIVO OU NEGATIVO ---")
try:
    valor = float(input("Digite um valor numérico: "))
    
    # PONTO DE DECISÃO
    if valor >= 0:
        resultado = "Positivo (inclui zero)"
    else:
        resultado = "Negativo"
        
    print(f"Resultado:\n  O valor {valor} é: {resultado}\n")

except ValueError:
    print("ERRO: Digite apenas números válidos.")