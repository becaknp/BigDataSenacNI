### IMC
def calcular_imc(peso,altura):
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
    # if imc < 18.5:
        























#Ano bissexto

def eh_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

# Programa principal
try:
    ano = int(input("Digite um ano: "))
    
    if eh_bissexto(ano):
        print(f"O ano {ano} E bissexto")
    else:
        print(f"O ano {ano} NAO e bissexto")
        
except ValueError:
    print("Erro: Digite um numero valido!")


#### Contador

def contar_caractere(texto, caractere_procurado):
    texto = texto.lower()
    caractere_procurado = caractere_procurado.lower()
    
    contador = 0
    for letra in texto:
        if letra == caractere_procurado:
            contador += 1
    
    return contador

# Programa principal
try:
    frase = input("Digite uma frase: ")
    letra = input("Digite uma letra para contar: ")
    
    if len(letra) != 1:
        print("Erro: Digite apenas UM caractere!")
    else:
        resultado = contar_caractere(frase, letra)
        print(f"A letra '{letra}' aparece {resultado} vezes na frase.")
        
except Exception as e:
    print(f"Erro inesperado: {e}")