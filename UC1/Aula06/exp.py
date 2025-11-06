dados_entrada = []
print("Digite 5 nomes de filmes:")
for i in range(5):
 nome = input(f"Filme {i+1}: ")
 dados_entrada.append(nome) # Usando LISTA para coletar os dados
 
print("-" * 30)
#Armazenamento e Exibição:
# 1. LISTA:
lista_filmes = dados_entrada
# 2. TUPLA:
tupla_filmes = tuple(dados_entrada)
# 3. SET:
set_filmes = set(dados_entrada)
# 4. DICIONÁRIO: Usando o índice como chave (ex: 1: 'Filme A')
dicionario_filmes = {}
for i in range(len(dados_entrada)): # Repetição pelo tamanho da lista
 # Usando o índice (i+1) como CHAVE e o nome como VALOR
 dicionario_filmes[i + 1] = dados_entrada[i]
print(f"LISTA (Flexível): {lista_filmes}")
print(f"TUPLA (Fixa): {tupla_filmes}")
print(f"SET (Apenas Únicos): {set_filmes}")
print(f"DICIONÁRIO (Chave: Valor): {dicionario_filmes}")