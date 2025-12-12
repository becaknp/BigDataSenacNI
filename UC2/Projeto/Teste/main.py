# projeto_vendas_completo.py
import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, gaussian_kde
import os

# ============================================
# CONFIGURAÇÕES DO BANCO DE DADOS
# ============================================
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root', 
    'password': '',  
    'database': 'sales_online'
}

# ============================================
# CLASSE PARA CONEXÃO COM BANCO DE DADOS
# ============================================
class VendasDatabase:
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """Conecta ao banco de dados MySQL"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            print("Conectado ao banco de dados MySQL!")
            return True
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return False
    
    def disconnect(self):
        """Desconecta do banco de dados"""
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Conexao encerrada.")
    
    def execute_query(self, query, params=None, fetch=True):
        """Executa uma consulta SQL"""
        try:
            self.cursor.execute(query, params or ())
            if fetch:
                if query.strip().upper().startswith('SELECT'):
                    result = self.cursor.fetchall()
                    columns = [desc[0] for desc in self.cursor.description]
                    return pd.DataFrame(result, columns=columns)
                else:
                    self.connection.commit()
                    return True
        except Error as e:
            print(f"Erro na consulta: {e}")
            return None

# ============================================
# FUNÇÕES AUXILIARES
# ============================================
def encontrar_arquivos_csv():
    """Tenta encontrar os arquivos CSV automaticamente"""
    arquivos_procurados = ['Online_Sales_Data.csv', 'Customer.csv']
    caminhos_possiveis = ['.', '..', './data', '../data']
    
    for caminho_base in caminhos_possiveis:
        encontrados = True
        caminhos_completos = []
        
        for arquivo in arquivos_procurados:
            caminho_completo = os.path.join(caminho_base, arquivo)
            if os.path.exists(caminho_completo):
                caminhos_completos.append(caminho_completo)
            else:
                encontrados = False
                break
        
        if encontrados and len(caminhos_completos) == 2:
            print(f"Arquivos encontrados em: {caminho_base}")
            return caminhos_completos[0], caminhos_completos[1]
    
    print("Arquivos CSV nao encontrados. Usando dados de exemplo.")
    return None, None

# ============================================
# EXERCÍCIOS 1 e 2: CONSULTAS BÁSICAS
# ============================================
def exercicios_1_2(db):
    """Resolve os exercicios 1 e 2"""
    print("\n" + "="*50)
    print("EXERCICIOS 1 e 2: CONSULTAS BASICAS")
    print("="*50)
    
    # 1.5 e 2.5: Liste o nome de todos os elementos
    print("\n1. Nome de todos os produtos:")
    query1 = "SELECT DISTINCT Product_Name FROM Online_Sales_Data ORDER BY Product_Name"
    df_produtos = db.execute_query(query1)
    
    if df_produtos is not None:
        print(f"Total de produtos unicos: {len(df_produtos)}")
        print("Primeiros 10 produtos:")
        print(df_produtos.head(10).to_string(index=False))
    else:
        print("Nenhum produto encontrado ou erro na consulta")
    
    # 1.5 e 2.5: Nome e valor quantitativo
    print("\n2. Nome dos produtos e quantidade vendida:")
    query2 = """
    SELECT Product_Name, Units_Sold, Total_Revenue 
    FROM Online_Sales_Data 
    ORDER BY Units_Sold DESC 
    LIMIT 10
    """
    df_vendas = db.execute_query(query2)
    
    if df_vendas is not None:
        print("Top 10 produtos por quantidade vendida:")
        print(df_vendas.to_string(index=False))
    else:
        print("Erro na consulta de vendas")
    
    # 1.5 e 2.5: Contar elementos por filtro de categoria
    print("\n3. Quantidade de elementos por categoria:")
    query3 = """
    SELECT Product_Category, COUNT(*) as total_produtos
    FROM Online_Sales_Data 
    GROUP BY Product_Category 
    ORDER BY total_produtos DESC
    """
    df_categorias = db.execute_query(query3)
    
    if df_categorias is not None:
        print(df_categorias.to_string(index=False))
    else:
        print("Erro na consulta de categorias")
    
    return df_produtos, df_vendas, df_categorias

# ============================================
# EXERCÍCIO 3: CONSULTAS COM JOIN
# ============================================
def exercicio_3(db):
    """Executa 3 consultas utilizando JOIN entre as tabelas"""
    print("\n" + "="*50)
    print("EXERCICIO 3: CONSULTAS COM JOIN")
    print("="*50)
    
    # Consulta 1: Clientes com detalhes de suas transacoes
    print("\n1. Clientes e seus gastos totais:")
    query1 = """
    SELECT 
        c.Customer_Name,
        c.Email,
        c.Region as cliente_region,
        o.Product_Category,
        COUNT(o.Transactions_ID) as total_compras,
        SUM(o.Total_Revenue) as gasto_total,
        AVG(o.Unit_Price) as preco_medio
    FROM Customer c
    JOIN Online_Sales_Data o ON c.Transactions_ID = o.Transactions_ID
    GROUP BY c.Customer_Name, c.Email, c.Region, o.Product_Category
    ORDER BY gasto_total DESC
    LIMIT 10
    """
    df_join1 = db.execute_query(query1)
    if df_join1 is not None:
        print(df_join1.to_string(index=False))
    
    # Consulta 2: Métodos de pagamento por região
    print("\n2. Metodos de pagamento preferidos por regiao:")
    query2 = """
    SELECT 
        o.Region,
        o.Payment_Method,
        COUNT(*) as total_transacoes,
        SUM(o.Total_Revenue) as valor_total
    FROM Online_Sales_Data o
    GROUP BY o.Region, o.Payment_Method
    ORDER BY o.Region, total_transacoes DESC
    """
    df_join2 = db.execute_query(query2)
    if df_join2 is not None:
        print(df_join2.to_string(index=False))
    
    # Consulta 3: Produtos mais vendidos com informações de clientes
    print("\n3. Produtos mais populares por regiao:")
    query3 = """
    SELECT 
        o.Product_Name,
        o.Product_Category,
        c.Region,
        COUNT(*) as vezes_comprado,
        SUM(o.Units_Sold) as unidades_vendidas,
        SUM(o.Total_Revenue) as receita_total,
        COUNT(DISTINCT c.Customer_Name) as clientes_unicos
    FROM Online_Sales_Data o
    JOIN Customer c ON o.Transactions_ID = c.Transactions_ID
    GROUP BY o.Product_Name, o.Product_Category, c.Region
    HAVING unidades_vendidas > 10
    ORDER BY unidades_vendidas DESC
    LIMIT 10
    """
    df_join3 = db.execute_query(query3)
    if df_join3 is not None:
        print(df_join3.to_string(index=False))
    
    return df_join1, df_join2, df_join3

# ============================================
# EXERCÍCIO 4: PD.MERGE()
# ============================================
def exercicio_4():
    """Relaciona os DataFrames usando pd.merge()"""
    print("\n" + "="*50)
    print("EXERCICIO 4: PD.MERGE()")
    print("="*50)
    
    caminho_transacoes, caminho_clientes = encontrar_arquivos_csv()
    
    if caminho_transacoes and caminho_clientes:
        try:
            df_transacoes = pd.read_csv(caminho_transacoes)
            df_clientes = pd.read_csv(caminho_clientes)
            print("Arquivos CSV carregados com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar arquivos: {e}")
            return criar_dados_exemplo()
    else:
        return criar_dados_exemplo()
    
    # Padronizar nomes das colunas
    df_transacoes = df_transacoes.rename(columns={
        'Transaction_ID': 'Transactions_ID',
        'Date_transaction': 'Date_transaction',
        'Product_Category': 'Product_Category',
        'Product_Name': 'Product_Name',
        'Units_Sold': 'Units_Sold',
        'Unit_Price': 'Unit_Price',
        'Total_Revenue': 'Total_Revenue',
        'Region': 'Region',
        'Payment_Method': 'Payment_Method'
    })
    
    df_clientes = df_clientes.rename(columns={
        'Transaction_ID': 'Transactions_ID',
        'Customer_Name': 'Customer_Name',
        'Email': 'Email',
        'Product_Name': 'Product_Name',
        'Units_Sold': 'Units_Sold',
        'Date_transaction': 'Date_transaction',
        'Region': 'Region'
    })
    
    # Merge das tabelas
    df_merged = pd.merge(
        df_transacoes,
        df_clientes,
        on='Transactions_ID',
        how='inner',
        suffixes=('_trans', '_cli')
    )
    
    print(f"Shape apos merge: {df_merged.shape}")
    print(f"Total de transacoes combinadas: {len(df_merged)}")
    
    if len(df_merged) > 0:
        print("\nPrimeiras 5 linhas do DataFrame merged:")
        colunas_mostrar = ['Transactions_ID', 'Customer_Name', 'Product_Name_trans', 
                          'Total_Revenue', 'Region_trans', 'Payment_Method']
        colunas_disponiveis = [col for col in colunas_mostrar if col in df_merged.columns]
        print(df_merged[colunas_disponiveis].head().to_string(index=False))
        
        if 'Customer_Name' in df_merged.columns and 'Total_Revenue' in df_merged.columns:
            print("\nAnalise: Top 5 clientes que mais gastaram:")
            top_clientes = df_merged.groupby('Customer_Name')['Total_Revenue'].sum().nlargest(5)
            print(top_clientes.to_string())
    
    return df_merged

def criar_dados_exemplo():
    """Cria dados de exemplo para demonstracao"""
    print("Criando dados de exemplo para demonstracao...")
    
    dados_transacoes = pd.DataFrame({
        'Transactions_ID': range(10001, 10021),
        'Date_transaction': pd.date_range('2024-01-01', periods=20),
        'Product_Category': ['Electronics']*5 + ['Clothing']*5 + ['Home']*5 + ['Books']*5,
        'Product_Name': ['iPhone 14', 'MacBook', 'Samsung TV', 'iPad', 'Apple Watch',
                        'T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Dress',
                        'Vacuum', 'Blender', 'Microwave', 'Coffee Maker', 'Toaster',
                        'Python Book', 'SQL Guide', 'Data Science', 'AI Basics', 'ML Advanced'],
        'Units_Sold': np.random.randint(1, 10, 20),
        'Unit_Price': np.random.uniform(50, 1000, 20),
        'Total_Revenue': np.random.uniform(100, 5000, 20),
        'Region': ['North America']*7 + ['Europe']*6 + ['Asia']*7,
        'Payment_Method': ['Credit Card']*10 + ['PayPal']*10
    })
    
    dados_clientes = pd.DataFrame({
        'Transactions_ID': range(10001, 10021),
        'Customer_Name': [f'Cliente_{i}' for i in range(1, 21)],
        'Email': [f'cliente{i}@email.com' for i in range(1, 21)],
        'Product_Name': dados_transacoes['Product_Name'].values,
        'Units_Sold': dados_transacoes['Units_Sold'].values,
        'Date_transaction': dados_transacoes['Date_transaction'].values,
        'Region': dados_transacoes['Region'].values
    })
    
    dados_transacoes['Total_Revenue'] = dados_transacoes['Units_Sold'] * dados_transacoes['Unit_Price']
    
    df_merged_exemplo = pd.merge(
        dados_transacoes,
        dados_clientes,
        on='Transactions_ID',
        suffixes=('_trans', '_cli')
    )
    
    print(f"Dados de exemplo criados: {len(df_merged_exemplo)} registros")
    print("\nExemplo do resultado do merge:")
    print(df_merged_exemplo[['Transactions_ID', 'Customer_Name', 'Product_Name_trans', 
                            'Total_Revenue', 'Region_trans']].head().to_string(index=False))
    
    return df_merged_exemplo

# ============================================
# EXERCÍCIOS 5, 6 e 7: ANÁLISE ESTATÍSTICA BÁSICA
# ============================================
def exercicios_5_6_7(df_merged):
    """Executa analises estatisticas e deteccao de outliers"""
    print("\n" + "="*50)
    print("EXERCICIOS 5, 6 e 7: ANALISE ESTATISTICA BASICA")
    print("="*50)
    
    if 'Total_Revenue' not in df_merged.columns:
        print("Erro: Coluna 'Total_Revenue' nao encontrada no DataFrame.")
        return None
    
    revenue_data = df_merged['Total_Revenue'].values
    revenue_array = np.array(revenue_data, dtype=float)
    
    # 5.3 Calcular media e mediana
    media = np.mean(revenue_array)
    mediana = np.median(revenue_array)
    
    print(f"5.3 Estatisticas da Receita Total:")
    print(f"Média: ${media:.2f}")
    print(f"Mediana: ${mediana:.2f}")
    
    # 5.4 Calcular distancia entre media e mediana
    distancia = abs(media - mediana)
    print(f"\n5.4 Distancia entre media e mediana: ${distancia:.2f}")
    
    # 5.5 Interpretacao
    print("\n5.5 Interpretacao:")
    if distancia < media * 0.1:
        print("A distribuicao e aproximadamente simetrica.")
    elif media > mediana:
        print("A distribuicao tem assimetria positiva (a direita).")
        print("Ha alguns valores muito altos que puxam a media para cima.")
    else:
        print("A distribuicao tem assimetria negativa (a esquerda).")
    
    # 6. Deteccao de outliers usando IQR
    print("\n6. DETECCAO DE OUTLIERS (METODO IQR)")
    
    Q1 = np.percentile(revenue_array, 25)
    Q3 = np.percentile(revenue_array, 75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    print(f"Q1 (25º percentil): ${Q1:.2f}")
    print(f"Q3 (75º percentil): ${Q3:.2f}")
    print(f"IQR: ${IQR:.2f}")
    print(f"Limite inferior: ${limite_inferior:.2f}")
    print(f"Limite superior: ${limite_superior:.2f}")
    
    outliers_inferiores = revenue_array[revenue_array < limite_inferior]
    outliers_superiores = revenue_array[revenue_array > limite_superior]
    
    # 7. Apresentar resultados
    print("\n7. RESULTADOS DOS OUTLIERS:")
    print(f"Total de outliers: {len(outliers_inferiores) + len(outliers_superiores)}")
    print(f"Outliers inferiores: {len(outliers_inferiores)}")
    if len(outliers_inferiores) > 0:
        print(f"Valores: {outliers_inferiores}")
    
    print(f"\nOutliers superiores: {len(outliers_superiores)}")
    if len(outliers_superiores) > 0:
        print(f"Valores (5 primeiros): {outliers_superiores[:5]}")
        print(f"Maximo outlier: ${np.max(outliers_superiores):.2f}")
    
    percentual_outliers = (len(outliers_inferiores) + len(outliers_superiores)) / len(revenue_array) * 100
    print(f"\nPercentual de outliers: {percentual_outliers:.2f}%")
    
    return revenue_array, media, mediana, outliers_superiores, outliers_inferiores

# ============================================
# EXERCÍCIO 8: VARIABILIDADE DOS PREÇOS (AULA 08) - CORRIGIDO
# ============================================
def exercicio_8_variabilidade_precos(db):
    """
    Exercício 8: Analisa a variabilidade dos preços unitários dos produtos
    Aplica conceitos da Aula 08: Variância, Desvio Padrão e Coeficiente de Variação
    """
    print("\n" + "="*70)
    print("EXERCICIO 8: ANALISE DE VARIABILIDADE DOS PRECOS (AULA 08)")
    print("="*70)
    
    query_precos = """
    SELECT Unit_Price 
    FROM Online_Sales_Data 
    WHERE Unit_Price > 0
    ORDER BY Unit_Price
    """
    
    df_precos = db.execute_query(query_precos)
    
    if df_precos is None or len(df_precos) == 0:
        print("Erro: Nao foi possivel obter dados de precos.")
        return None
    
    precos_array = df_precos['Unit_Price'].values
    
    print(f"Total de precos analisados: {len(precos_array)}")
    print(f"Preco minimo: ${precos_array.min():.2f}")
    print(f"Preco maximo: ${precos_array.max():.2f}")
    
    # 1. Medidas de tendencia central
    media = np.mean(precos_array)
    mediana = np.median(precos_array)
    
    print("\n" + "-"*50)
    print("1. MEDIDAS DE TENDENCIA CENTRAL")
    print("-"*50)
    print(f"Média dos precos: ${media:.2f}")
    print(f"Mediana dos precos: ${mediana:.2f}")
    
    # 2. Medidas de dispersão
    variancia = np.var(precos_array)
    desvio_padrao = np.std(precos_array)
    
    print("\n" + "-"*50)
    print("2. MEDIDAS DE DISPERSAO (Aula 08)")
    print("-"*50)
    print(f"Variancia dos precos: ${variancia:.2f}")
    print(f"Desvio Padrao dos precos: ${desvio_padrao:.2f}")
    
    # 3. Coeficiente de Variação (CV)
    cv = (desvio_padrao / media) * 100 if media != 0 else 0
    
    print("\n" + "-"*50)
    print("3. COEFICIENTE DE VARIACAO (CV)")
    print("-"*50)
    print(f"Coeficiente de Variacao (CV): {cv:.2f}%")
    
    if cv < 15:
        interpretacao_cv = "Baixa variabilidade (precos estaveis)"
    elif cv < 30:
        interpretacao_cv = "Variabilidade moderada"
    else:
        interpretacao_cv = "Alta variabilidade (precos muito dispersos)"
    
    print(f"Interpretacao: {interpretacao_cv}")
    
    # 4. Distância da Variância em relação à Média
    distancia_variancia = variancia / (media ** 2) if media != 0 else 0
    
    print("\n" + "-"*50)
    print("4. DISTANCIA DA VARIANCIA EM RELACAO A MEDIA")
    print("-"*50)
    print(f"Distancia (Variancia / Media²): {distancia_variancia:.4f}")
    
    if distancia_variancia <= 0.10:
        analise_dispersao = "BAIXA DISPERSAO - Os precos estao muito proximos da media"
    elif distancia_variancia < 0.25:
        analise_dispersao = "DISPERSAO MODERADA - Os precos tem variacao media"
    else:
        analise_dispersao = "ALTA DISPERSAO - Os precos estao muito espalhados"
    
    print(f"Analise de Dispersao: {analise_dispersao}")
    
    # 5. Tabela de distribuição por faixa de preço - CORRIGIDO
    print("\n" + "-"*50)
    print("5. DISTRIBUICAO DE PRECOS POR FAIXA")
    print("-"*50)
    
    faixas = [0, 50, 100, 200, 500, 1000, 2000, 5000, np.inf]
    rotulos = ['$0-50', '$51-100', '$101-200', '$201-500', '$501-1000', 
              '$1001-2000', '$2001-5000', 'Acima $5000']
    
    # Método corrigido que funciona em todas as versões do pandas
    precos_series = pd.Series(precos_array)
    categorias = pd.cut(precos_series, bins=faixas, labels=rotulos, right=False)
    
    # Contagem sem usar normalize
    contagem = categorias.value_counts().sort_index()
    total = len(precos_array)
    
    df_distribuicao = pd.DataFrame({
        'Faixa de Preco': contagem.index.tolist(),
        'Quantidade': contagem.values,
        'Percentual': (contagem.values / total * 100)
    })
    
    print(df_distribuicao.to_string(index=False))
    
    # 6. Relação entre média e mediana
    print("\n" + "-"*50)
    print("6. RELACAO MEDIA vs MEDIANA")
    print("-"*50)
    
    diferenca_absoluta = abs(media - mediana)
    diferenca_relativa = (diferenca_absoluta / media) * 100 if media != 0 else 0
    
    print(f"Diferenca absoluta: ${diferenca_absoluta:.2f}")
    print(f"Diferenca relativa: {diferenca_relativa:.2f}%")
    
    if media > mediana:
        print("Interpretacao: Media > Mediana - Possivel cauda a direita (produtos caros)")
    elif media < mediana:
        print("Interpretacao: Media < Mediana - Possivel cauda a esquerda (produtos baratos)")
    else:
        print("Interpretacao: Media = Mediana - Distribuicao simetrica")
    
    return {
        'precos_array': precos_array,
        'media': media,
        'mediana': mediana,
        'variancia': variancia,
        'desvio_padrao': desvio_padrao,
        'cv': cv,
        'distancia_variancia': distancia_variancia,
        'df_distribuicao': df_distribuicao
    }

# ============================================
# EXERCÍCIO 9: ASSIMETRIA E CURTOSE (AULA 09) - CORRIGIDO
# ============================================
def exercicio_9_assimetria_curtose(db):
    """
    Exercício 9: Analisa a forma da distribuição das receitas totais
    Aplica conceitos da Aula 09: Assimetria e Curtose
    """
    print("\n" + "="*70)
    print("EXERCICIO 9: ANALISE DA FORMA DA DISTRIBUICAO (AULA 09)")
    print("="*70)
    
    query_receitas = """
    SELECT Total_Revenue 
    FROM Online_Sales_Data 
    WHERE Total_Revenue > 0
    ORDER BY Total_Revenue
    """
    
    df_receitas = db.execute_query(query_receitas)
    
    if df_receitas is None or len(df_receitas) == 0:
        print("Erro: Nao foi possivel obter dados de receitas.")
        return None
    
    receitas_array = df_receitas['Total_Revenue'].values
    
    print(f"Total de transacoes analisadas: {len(receitas_array)}")
    print(f"Receita minima: ${receitas_array.min():.2f}")
    print(f"Receita maxima: ${receitas_array.max():.2f}")
    print(f"Receita total: ${receitas_array.sum():.2f}")
    
    # 1. Calcular medidas básicas
    media = np.mean(receitas_array)
    mediana = np.median(receitas_array)
    desvio_padrao = np.std(receitas_array)
    
    print("\n" + "-"*50)
    print("1. MEDIDAS BASICAS DA RECEITA TOTAL")
    print("-"*50)
    print(f"Média: ${media:.2f}")
    print(f"Mediana: ${mediana:.2f}")
    print(f"Desvio Padrao: ${desvio_padrao:.2f}")
    
    # 2. Calcular Assimetria
    assimetria = skew(receitas_array)
    
    print("\n" + "-"*50)
    print("2. ASSIMETRIA (SKEWNESS) - Aula 09")
    print("-"*50)
    print(f"Assimetria: {assimetria:.4f}")
    
    print("\nInterpretacao da Assimetria:")
    print("-" * 30)
    
    if assimetria >= -0.5 and assimetria <= 0.5:
        print("Distribuicao: SIMETRICA ou QUASE SIMETRICA")
        print("Relacao Media vs Mediana: Media ≈ Mediana")
        print("Caracteristica: Dados distribuidos de forma equilibrada")
    elif assimetria > 0.5:
        print("Distribuicao: ASSIMETRICA POSITIVA (cauda a direita)")
        print(f"Relacao Media vs Mediana: Media (${media:.2f}) > Mediana (${mediana:.2f})")
        print("Caracteristica: Cauda se estende para valores maiores (receitas altas)")
        print("Implicacao: Poucas transacoes com valores muito altos 'puxam' a media para cima")
    else:
        print("Distribuicao: ASSIMETRICA NEGATIVA (cauda a esquerda)")
        print(f"Relacao Media vs Mediana: Media (${media:.2f}) < Mediana (${mediana:.2f})")
        print("Caracteristica: Cauda se estende para valores menores (receitas baixas)")
        print("Implicacao: Poucas transacoes com valores muito baixos 'puxam' a media para baixo")
    
    # 3. Calcular Curtose
    curtose_excesso = kurtosis(receitas_array, fisher=True)
    curtose_real = curtose_excesso + 3
    
    print("\n" + "-"*50)
    print("3. CURTOSE (KURTOSIS) - Aula 09")
    print("-"*50)
    print(f"Curtose em Excesso (Pandas): {curtose_excesso:.4f}")
    print(f"Curtose Real (Referencia 3.0): {curtose_real:.4f}")
    
    print("\nInterpretacao da Curtose:")
    print("-" * 30)
    
    if curtose_real >= 2.5 and curtose_real <= 3.5:
        print("Tipo: MESOCURTICA")
        print("Caracteristica: Distribuicao proxima da normal")
        print("Outliers: Menos comuns")
        print("Implicacao: Receitas distribuídas uniformemente em torno da media")
    elif curtose_real < 2.5:
        print("Tipo: PLATICURTICA")
        print("Caracteristica: Distribuicao mais achatada")
        print("Outliers: Comuns")
        print("Implicacao: Receitas mais dispersas, menos concentradas na media")
    else:
        print("Tipo: LEPTOCURTICA")
        print("Caracteristica: Distribuicao mais pontiaguda")
        print("Outliers: Muito comuns nas caudas")
        print("Implicacao: Receitas extremamente concentradas no centro, com muitos outliers")
    
    # 4. Tabela de Quartis e Outliers
    print("\n" + "-"*50)
    print("4. QUARTIS E DETECCAO DE OUTLIERS")
    print("-"*50)
    
    Q1 = np.percentile(receitas_array, 25)
    Q3 = np.percentile(receitas_array, 75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers_inferiores = receitas_array[receitas_array < limite_inferior]
    outliers_superiores = receitas_array[receitas_array > limite_superior]
    
    estatisticas = pd.DataFrame({
        'Medida': ['Q1 (25%)', 'Q3 (75%)', 'IQR', 'Limite Inferior', 'Limite Superior', 
                  'Minimo', 'Maximo', 'Outliers Inferiores', 'Outliers Superiores', 'Total Outliers'],
        'Valor': [f"${Q1:.2f}", f"${Q3:.2f}", f"${IQR:.2f}", 
                 f"${limite_inferior:.2f}", f"${limite_superior:.2f}",
                 f"${receitas_array.min():.2f}", f"${receitas_array.max():.2f}",
                 len(outliers_inferiores), len(outliers_superiores),
                 len(outliers_inferiores) + len(outliers_superiores)]
    })
    
    print(estatisticas.to_string(index=False))
    
    # 5. Distribuição por faixa de receita - CORRIGIDO
    print("\n" + "-"*50)
    print("5. DISTRIBUICAO DAS RECEITAS POR FAIXA")
    print("-"*50)
    
    faixas_receita = [0, 100, 500, 1000, 2000, 5000, np.inf]
    rotulos_receita = ['$0-100', '$101-500', '$501-1000', '$1001-2000', 
                      '$2001-5000', 'Acima $5000']
    
    # Método corrigido
    receitas_series = pd.Series(receitas_array)
    categorias_receita = pd.cut(receitas_series, bins=faixas_receita, labels=rotulos_receita, right=False)
    
    # Contagem sem normalize
    contagem_receita = categorias_receita.value_counts().sort_index()
    total_receitas = len(receitas_array)
    
    # Calcular receita acumulada por categoria
    receita_acumulada = []
    for rotulo in rotulos_receita:
        mascara = (categorias_receita == rotulo)
        receita_acumulada.append(receitas_array[mascara].sum())
    
    df_dist_receitas = pd.DataFrame({
        'Faixa de Receita': rotulos_receita,
        'Quantidade': contagem_receita.values,
        'Percentual': (contagem_receita.values / total_receitas * 100),
        'Receita Acumulada': receita_acumulada
    })
    
    receita_total = receitas_array.sum()
    df_dist_receitas['% Receita Total'] = (df_dist_receitas['Receita Acumulada'] / receita_total) * 100
    
    print(df_dist_receitas.to_string(index=False))
    
    # 6. Análise de concentração (Pareto)
    print("\n" + "-"*50)
    print("6. ANALISE DE CONCENTRACAO (PARETO)")
    print("-"*50)
    
    # Ordenar transações por valor (decrescente)
    transacoes_ordenadas = np.sort(receitas_array)[::-1]
    
    # Calcular receita acumulada
    receita_acumulada_total = np.cumsum(transacoes_ordenadas)
    receita_acumulada_percentual = (receita_acumulada_total / receita_total) * 100
    
    # Encontrar quantas transações geram 80% da receita
    idx_80_percent = np.where(receita_acumulada_percentual >= 80)[0]
    if len(idx_80_percent) > 0:
        n_transacoes_80 = idx_80_percent[0] + 1
        percentual_transacoes_80 = (n_transacoes_80 / len(transacoes_ordenadas)) * 100
        
        print(f"Transacoes que geram 80% da receita: {n_transacoes_80} transacoes")
        print(f"Isso representa: {percentual_transacoes_80:.1f}% do total de transacoes")
        
        if percentual_transacoes_80 < 20:
            print("PRINCIPIO DE PARETO APLICAVEL: 80% da receita vem de menos de 20% das transacoes")
        else:
            print("Distribuicao mais equilibrada: receita distribuida entre mais transacoes")
    
    # 7. Sugestões baseadas na análise
    print("\n" + "-"*50)
    print("7. SUGESTOES PARA GESTAO")
    print("-"*50)
    
    print("Baseado na analise da distribuicao das receitas:")
    
    if assimetria > 0.5:
        print("- A distribuicao e assimetrica positiva (cauda a direita)")
        print("- Sugestao: Focar em manter os clientes de alto valor (cauda direita)")
        print("- Acao: Criar programa de fidelidade para clientes premium")
    elif assimetria < -0.5:
        print("- A distribuicao e assimetrica negativa (cauda a esquerda)")
        print("- Sugestao: Tentar aumentar o valor medio das transacoes")
        print("- Acao: Implementar estrategias de upselling/cross-selling")
    else:
        print("- A distribuicao e simetrica")
        print("- Sugestao: Estrategias podem ser aplicadas uniformemente")
        print("- Acao: Manter mix balanceado de produtos")
    
    if curtose_real > 3.5:
        print("- Distribuicao leptocurtica (muitos outliers)")
        print("- Sugestao: Investigar transacoes extremas (outliers)")
        print("- Acao: Verificar se sao erros ou oportunidades de negocio")
    elif curtose_real < 2.5:
        print("- Distribuicao platicurtica (dados dispersos)")
        print("- Sugestao: Segmentar clientes por faixa de valor")
        print("- Acao: Criar estrategias especificas para cada segmento")
    
    return {
        'receitas_array': receitas_array,
        'media': media,
        'mediana': mediana,
        'assimetria': assimetria,
        'curtose_excesso': curtose_excesso,
        'curtose_real': curtose_real,
        'df_dist_receitas': df_dist_receitas,
        'estatisticas': estatisticas
    }

# ============================================
# FUNÇÕES AUXILIARES PARA VISUALIZAÇÃO
# ============================================
def gerar_visualizacoes_ex8(resultado):
    """Gera visualizacoes para o Exercicio 8"""
    try:
        precos_array = resultado['precos_array']
        media = resultado['media']
        mediana = resultado['mediana']
        
        # Histograma dos precos
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.hist(precos_array, bins=30, alpha=0.7, color='blue', edgecolor='black')
        plt.axvline(media, color='red', linestyle='--', label=f'Media: ${media:.2f}')
        plt.axvline(mediana, color='green', linestyle='--', label=f'Mediana: ${mediana:.2f}')
        plt.xlabel('Preco Unitario ($)')
        plt.ylabel('Frequencia')
        plt.title('Distribuicao dos Precos Unitarios')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Boxplot
        plt.subplot(1, 2, 2)
        plt.boxplot(precos_array, vert=True)
        plt.ylabel('Preco Unitario ($)')
        plt.title('Boxplot - Precos Unitarios')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('analise_precos.png', dpi=300, bbox_inches='tight')
        print("Visualizacoes salvas como 'analise_precos.png'")
        plt.show()
        
    except Exception as e:
        print(f"Erro ao gerar visualizacoes: {e}")

def gerar_visualizacoes_ex9(resultado):
    """Gera visualizacoes para o Exercicio 9"""
    try:
        receitas_array = resultado['receitas_array']
        media = resultado['media']
        mediana = resultado['mediana']
        assimetria = resultado['assimetria']
        curtose_real = resultado['curtose_real']
        
        # Histograma com KDE
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.hist(receitas_array, bins=30, alpha=0.7, color='purple', edgecolor='black', density=True)
        
        # Adicionar linha de densidade KDE
        kde = gaussian_kde(receitas_array)
        x_range = np.linspace(receitas_array.min(), receitas_array.max(), 1000)
        plt.plot(x_range, kde(x_range), 'r-', linewidth=2, label='Densidade (KDE)')
        
        plt.axvline(media, color='red', linestyle='--', label=f'Media: ${media:.2f}')
        plt.axvline(mediana, color='green', linestyle='--', label=f'Mediana: ${mediana:.2f}')
        plt.xlabel('Receita Total ($)')
        plt.ylabel('Densidade')
        plt.title(f'Distribuicao das Receitas\nAssimetria: {assimetria:.2f}, Curtose: {curtose_real:.2f}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # QQ-Plot para normalidade
        plt.subplot(1, 2, 2)
        from scipy import stats
        stats.probplot(receitas_array, dist="norm", plot=plt)
        plt.title('QQ-Plot para Normalidade')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('analise_receitas_distribuicao.png', dpi=300, bbox_inches='tight')
        print("Visualizacoes salvas como 'analise_receitas_distribuicao.png'")
        plt.show()
        
    except Exception as e:
        print(f"Erro ao gerar visualizacoes: {e}")

# ============================================
# FUNÇÃO PRINCIPAL COM MENU
# ============================================
def main():
    """Funcao principal do projeto"""
    print("="*70)
    print("PROJETO COMPLETO DE ANALISE DE DADOS - VENDAS ONLINE")
    print("MySQL + Python + Pandas + NumPy + Estatistica")
    print("="*70)
    
    # Criar instancia do banco de dados
    db = VendasDatabase()
    
    try:
        # Conectar ao banco de dados
        print("\nConectando ao banco de dados...")
        if not db.connect():
            print("Falha na conexao com o banco. Verifique as credenciais.")
            return
        
        # Menu de exercicios
        print("\n" + "="*70)
        print("MENU DE EXERCICIOS")
        print("="*70)
        print("1. Exercicios 1-2: Consultas basicas")
        print("2. Exercicio 3: JOINs SQL")
        print("3. Exercicio 4: pd.merge()")
        print("4. Exercicios 5-7: Analise estatistica basica")
        print("5. Exercicio 8: Variabilidade dos Precos (Aula 08)")
        print("6. Exercicio 9: Assimetria e Curtose (Aula 09)")
        print("7. Todos os exercicios")
        print("="*70)
        
        escolha = input("\nEscolha uma opcao (1-7): ").strip()
        
        if escolha == '1':
            exercicios_1_2(db)
        elif escolha == '2':
            exercicio_3(db)
        elif escolha == '3':
            exercicio_4()
        elif escolha == '4':
            df_merged = exercicio_4()
            if df_merged is not None:
                exercicios_5_6_7(df_merged)
        elif escolha == '5':
            resultado_ex8 = exercicio_8_variabilidade_precos(db)
            if resultado_ex8:
                gerar_visualizacoes_ex8(resultado_ex8)
        elif escolha == '6':
            resultado_ex9 = exercicio_9_assimetria_curtose(db)
            if resultado_ex9:
                gerar_visualizacoes_ex9(resultado_ex9)
        elif escolha == '7':
            # Executar todos
            print("\nExecutando todos os exercicios...")
            print("\n" + "="*70)
            print("EXERCICIOS 1-2: CONSULTAS BASICAS")
            print("="*70)
            exercicios_1_2(db)
            
            input("\nPressione Enter para continuar com o Exercicio 3...")
            print("\n" + "="*70)
            print("EXERCICIO 3: JOINS SQL")
            print("="*70)
            exercicio_3(db)
            
            input("\nPressione Enter para continuar com o Exercicio 4...")
            print("\n" + "="*70)
            print("EXERCICIO 4: PD.MERGE()")
            print("="*70)
            df_merged = exercicio_4()
            
            if df_merged is not None:
                input("\nPressione Enter para continuar com os Exercicios 5-7...")
                print("\n" + "="*70)
                print("EXERCICIOS 5-7: ANALISE ESTATISTICA BASICA")
                print("="*70)
                exercicios_5_6_7(df_merged)
            
            input("\nPressione Enter para continuar com o Exercicio 8...")
            print("\n" + "="*70)
            print("EXERCICIO 8: VARIABILIDADE DOS PRECOS (AULA 08)")
            print("="*70)
            resultado_ex8 = exercicio_8_variabilidade_precos(db)
            if resultado_ex8:
                gerar_visualizacoes_ex8(resultado_ex8)
            
            input("\nPressione Enter para continuar com o Exercicio 9...")
            print("\n" + "="*70)
            print("EXERCICIO 9: ASSIMETRIA E CURTOSE (AULA 09)")
            print("="*70)
            resultado_ex9 = exercicio_9_assimetria_curtose(db)
            if resultado_ex9:
                gerar_visualizacoes_ex9(resultado_ex9)
        else:
            print("Opcao invalida. Executando todos os exercicios por padrao.")
            exercicios_1_2(db)
            exercicio_3(db)
            df_merged = exercicio_4()
            if df_merged is not None:
                exercicios_5_6_7(df_merged)
            resultado_ex8 = exercicio_8_variabilidade_precos(db)
            if resultado_ex8:
                gerar_visualizacoes_ex8(resultado_ex8)
            resultado_ex9 = exercicio_9_assimetria_curtose(db)
            if resultado_ex9:
                gerar_visualizacoes_ex9(resultado_ex9)
        
        print("\n" + "="*70)
        print("PROJETO CONCLUIDO COM SUCESSO!")
        print("="*70)
        
    except Exception as e:
        print(f"\nErro durante a execucao: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Desconectar do banco de dados
        db.disconnect()

# ============================================
# EXECUÇÃO PRINCIPAL
# ============================================
if __name__ == "__main__":
    main()