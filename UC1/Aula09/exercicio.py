"""
Este programa calcula a multa de um pescador baseado no peso pescado
e inclui o desafio de acumular multas de várias pescarias.
"""

# --- Definição da Função ---

def calcular_multa(peso_total):
    """
    Recebe o peso total de peixes e retorna o valor da multa.
    - Limite: 100 kg
    - Multa: R$ 4,00 por kg excedente
    """
    LIMITE_KG = 100.0
    VALOR_MULTA_POR_KG = 4.00
    
    if peso_total > LIMITE_KG:
        # Calcula o quanto passou do limite
        excesso = peso_total - LIMITE_KG
        # Calcula a multa
        multa = excesso * VALOR_MULTA_POR_KG
        return multa
    else:
        # Se não passou do limite, a multa é zero
        return 0.0

# --- Programa Principal ---

# Variável para guardar o total de multas do dia
multa_total_dia = 0.0
print("--- Controle de Produtividade da Pesca ---")
print("(Digite 0 no peso para encerrar o dia)")

# Loop 'while' para perguntar o peso de várias pescarias
while True:
    try:
        peso_da_pescaria = float(input("\nDigite o peso da pescaria (kg): "))
        
        # Condição de parada do loop
        if peso_da_pescaria == 0:
            print("Encerrando o dia...")
            break
            
        # 1. Chama a função com o peso informado
        multa_da_vez = calcular_multa(peso_da_pescaria)
        
        # 2. Verifica o valor retornado pela função
        if multa_da_vez > 0:
            # Mostra a multa formatada com 2 casas decimais
            print(f"Multa desta pescaria: R$ {multa_da_vez:.2f}")
        else:
            # Mensagem caso não haja multa
            print("Peso dentro do limite. Nenhuma multa a pagar.")
            
        # 3. Acumula a multa da vez no total do dia
        multa_total_dia = multa_total_dia + multa_da_vez

    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

# --- Fim do loop ---

# Ao sair do loop, mostra o total acumulado
print("\n--- Resumo do Dia ---")
print(f"Total de multas acumulado no dia: R$ {multa_total_dia:.2f}")

########################

"""
Este programa calcula o IMC e a classificação de 'N' pessoas,
utilizando duas funções separadas para o cálculo e a classificação.
"""

# --- Definição das Funções ---

def calcular_imc(peso, altura):
    """
    Recebe peso (kg) e altura (m) e retorna o valor do IMC.
    Fórmula: IMC = PESO / (ALTURA * ALTURA)
    """
    if altura <= 0:
        print("Altura inválida. Não é possível calcular.")
        return 0.0
        
    imc = peso / (altura * altura)
    return imc

def obter_classificacao(imc):
    """
    Recebe um valor de IMC e retorna a string da classificação.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:  # Já sabemos que é >= 18.5
        return "Peso normal"
    elif imc < 30:  # Já sabemos que é >= 25
        return "Sobrepeso"
    else:           # Qualquer valor >= 30
        return "Obesidade"

# --- Programa Principal ---

print("--- Calculadora de IMC para N Pessoas ---")

try:
    # Pergunta quantas pessoas são
    n_pessoas = int(input("Quantas pessoas você deseja calcular? "))
    
    if n_pessoas <= 0:
        print("Número inválido. Encerrando.")
    else:
        # Faz um loop 'N' vezes
        for i in range(1, n_pessoas + 1):
            print(f"\n--- Dados da Pessoa {i} ---")
            
            # Coleta os dados dentro do loop
            try:
                peso = float(input(f"Digite o peso (kg) da pessoa {i}: "))
                altura = float(input(f"Digite a altura (m) da pessoa {i} (ex: 1.75): "))
                
                # 1. Chama a Função 1
                imc_calculado = calcular_imc(peso, altura)
                
                # Só continua se o IMC for válido
                if imc_calculado > 0:
                    # 2. Chama a Função 2 com o resultado da Função 1
                    classificacao = obter_classificacao(imc_calculado)
                    lista_consulta=[]
                    consultas=tuple(lista_consulta)
                    # 3. Imprime o resultado formatado
                    print(f"Resultado Pessoa {i}:")
                    print(f"  IMC: {imc_calculado:.2f}")
                    print(f"  Classificação: {classificacao}")

            except ValueError:
                print("Valores de peso ou altura inválidos. Pulando para a próxima pessoa.")

except ValueError:
    print("Número de pessoas inválido. Encerrando.")

print("\n--- Fim dos cálculos ---")

#####################

"""
Este programa permite ao usuário converter temperaturas entre
Celsius e Fahrenheit usando um menu e duas funções dedicadas.
"""

# --- Definição das Funções ---

def celsius_para_fahrenheit(temp_c):
    """
    Recebe temperatura em Celsius e retorna em Fahrenheit.
    Fórmula: F = (C * 9/5) + 32
    """
    temp_f = (temp_c * 9/5) + 32
    return temp_f

def fahrenheit_para_celsius(temp_f):
    """
    Recebe temperatura em Fahrenheit e retorna em Celsius.
    Fórmula: C = (F - 32) * 5/9
    """
    temp_c = (temp_f - 32) * 5/9
    return temp_c

# --- Programa Principal (Menu Interativo) ---

print("--- Conversor de Temperaturas ---")

# Loop 'while True' para manter o menu ativo
while True:
    # 1. Mostra o menu de opções
    print("\nEscolha uma opção:")
    print("1: Converter de Celsius para Fahrenheit")
    print("2: Converter de Fahrenheit para Celsius")
    print("3: Sair do programa")
    
    escolha = input("Digite sua escolha (1, 2 ou 3): ")
    
    try:
        # 2. Processa a escolha do usuário
        if escolha == '1':
            temp_c = float(input("Digite a temperatura em Celsius: "))
            # Chama a Função 1
            temp_f = celsius_para_fahrenheit(temp_c)
            # Mostra o resultado formatado com 1 casa decimal
            print(f"Resultado: {temp_c}°C é igual a {temp_f:.1f}°F")
            
        elif escolha == '2':
            temp_f = float(input("Digite a temperatura em Fahrenheit: "))
            # Chama a Função 2
            temp_c = fahrenheit_para_celsius(temp_f)
            # Mostra o resultado formatado com 1 casa decimal
            print(f"Resultado: {temp_f}°F é igual a {temp_c:.1f}°C")
            
        elif escolha == '3':
            # Condição de parada do loop
            print("Encerrando o programa...")
            break
            
        else:
            # Trata opções que não são 1, 2 ou 3
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
            
    except ValueError:
        # Trata o caso do usuário digitar "abc" em vez de um número
        print("Entrada inválida. Por favor, digite um número para a temperatura.")

#####################

"""
Este programa define uma função que verifica se um ano é bissexto
e pede um ano ao usuário para testar a função.
"""

# --- Definição da Função ---

def eh_bissexto(ano):
    """
    Recebe um ano (int) e retorna True se for bissexto, False caso contrário.
    
    Regras:
    1. Divisível por 4
    2. Exceto se for divisível por 100
    3. A menos que seja também divisível por 400
    """
    
    # Esta é a forma mais "Pythonica" de escrever a lógica
    # (É divisível por 4 E não é por 100) OU (É divisível por 400)
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# --- Programa Principal ---

print("--- Verificador de Ano Bissexto ---")

try:
    # 1. Peça um ano ao usuário
    ano_usuario = int(input("Digite um ano para verificar (ex: 2024): "))
    
    # 2. Chame a função e guarde o resultado (True ou False)
    resultado = eh_bissexto(ano_usuario)
    
    # 3. Imprima o resultado baseado no retorno da função
    if resultado: # Se 'resultado' for True
        print(f"O ano {ano_usuario} É bissexto.")
    else: # Se 'resultado' for False
        print(f"O ano {ano_usuario} NÃO é bissexto.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

################
    
"""
Este programa define uma função que conta a ocorrência de uma letra
em um texto (sem diferenciar maiúsculas/minúsculas).
"""

# --- Definição da Função ---

def contar_caractere(texto, caractere_procurado):
    """
    Recebe um texto e um caractere, e retorna quantas vezes
    o caractere aparece no texto (case-insensitive).
    """
    
    # Converte tudo para minúsculas para não diferenciar
    texto_lower = texto.lower()
    caractere_lower = caractere_procurado.lower()
    
    # Variável para guardar a contagem
    contador = 0
    
    # Loop 'for' para percorrer o texto
    for char in texto_lower:
        # Se o caractere atual for o que procuramos...
        if char == caractere_lower:
            contador = contador + 1
            
    # Retorna o total da contagem
    return contador

# --- Programa Principal ---

print("--- Contador de Letras ---")

# 1. Peça a frase ao usuário
frase = input("Digite uma frase: ")

# 2. Peça a letra que ele quer contar
#    Usamos [0] para garantir que pegamos apenas o primeiro caractere
letra = input("Digite a letra que deseja contar: ")[0] 

# 3. Chame a função com os dados do usuário
total_ocorrencias = contar_caractere(frase, letra)

# 4. Mostre o resultado
print(f"A letra '{letra}' (ou '{letra.upper()}') aparece {total_ocorrencias} vez(es) na sua frase.")

################

"""
Este programa define uma função que conta a ocorrência de uma letra
em um texto (sem diferenciar maiúsculas/minúsculas).
"""

# --- Definição da Função ---

def contar_caractere(texto, caractere_procurado):
    """
    Recebe um texto e um caractere, e retorna quantas vezes
    o caractere aparece no texto (case-insensitive).
    """
    
    # Converte tudo para minúsculas para não diferenciar
    texto_lower = texto.lower()
    caractere_lower = caractere_procurado.lower()
    
    # Variável para guardar a contagem
    contador = 0
    
    # Loop 'for' para percorrer o texto
    for char in texto_lower:
        # Se o caractere atual for o que procuramos...
        if char == caractere_lower:
            contador = contador + 1
            
    # Retorna o total da contagem
    return contador

# --- Programa Principal ---

print("--- Contador de Letras ---")

# 1. Peça a frase ao usuário
frase = input("Digite uma frase: ")

# 2. Peça a letra que ele quer contar
#    Usamos [0] para garantir que pegamos apenas o primeiro caractere
letra = input("Digite a letra que deseja contar: ")[0] 

# 3. Chame a função com os dados do usuário
total_ocorrencias = contar_caractere(frase, letra)

# 4. Mostre o resultado
print(f"A letra '{letra}' (ou '{letra.upper()}') aparece {total_ocorrencias} vez(es) na sua frase.")

################

