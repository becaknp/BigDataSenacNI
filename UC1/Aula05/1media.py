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