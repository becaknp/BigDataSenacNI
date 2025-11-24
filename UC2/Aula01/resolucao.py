import pandas as pd

# Carregar os dados do arquivo Excel.
df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

# --- Pergunta 1: Quais são as máximas e mínimas de operação de compra e venda das transações? ---

# Para encontrar o máximo e o mínimo para 'preco' e 'quantidade', filtre o DataFrame pela coluna 'operacao'.
df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']

# Use .max() e .min() para encontrar os valores mais altos e mais baixos nas colunas 'preco' e 'quantidade'.
max_compra_preco = df_compra['preco'].max()
min_compra_preco = df_compra['preco'].min()
max_venda_preco = df_venda['preco'].max()
min_venda_preco = df_venda['preco'].min()

print("--- Preços máximos e mínimos das operações ---")
print(f"Preço máximo de compra: {max_compra_preco}")
print(f"Preço mínimo de compra: {min_compra_preco}")
print(f"Preço máximo de venda: {max_venda_preco}")
print(f"Preço mínimo de venda: {min_venda_preco}")
print("\n")


# --- Pergunta 2: Qual CNPJ tem o ativo de maior valor? ---

# Primeiro, calcule o valor total de cada transação (quantidade * preço).
df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']

# Em seguida, agrupe as transações por 'id_ativo' para encontrar o valor total de cada ativo.
valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()

# Encontre o 'id_ativo' com o maior valor total.
id_ativo_maior_valor = valor_por_ativo.idxmax()

# Para obter o CNPJ, mescle o DataFrame `df_ativo` com o resultado.
cnpj_maior_valor = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

print("--- CNPJ com o ativo de maior valor ---")
print(f"O CNPJ para o ativo com o maior valor total é: {cnpj_maior_valor}")
print("\n")


# --- Pergunta 3: Qual valor total em transações de cada participante? ---

# Use .groupby() em 'id_participante' e depois .sum() na coluna 'valor_total'.
valor_por_participante = df_transacoes.groupby('id_participante')['valor_total'].sum()

print("--- Valor total de transação de cada participante ---")
print(valor_por_participante)
