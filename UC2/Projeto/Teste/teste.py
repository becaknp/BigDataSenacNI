# main_professor.py
# Análise estatística com as funções do professor
import pandas as pd
import numpy as np
from statistic import calcular_medidas_descritivas, gerar_painel_boxplot

def main():
    print("="*60)
    print("ANÁLISE ESTATÍSTICA - CÓDIGO DO PROFESSOR")
    print("="*60)
    
    # 1. Definir o caminho do arquivo
    # Coloque os arquivos CSV na mesma pasta deste script
    caminho_csv = "C:/Users/rebeca.knupp/OneDrive - SENAC RIO/UC2/Projeto/Sales DB/Online_Sales_Data.csv"
    
    # 2. Carregar os dados
    try:
        print(f"Carregando arquivo: {caminho_csv}")
        df = pd.read_csv(caminho_csv)
        
        print(f"\nArquivo carregado com sucesso!")
        print(f"Número de linhas: {len(df)}")
        print(f"\nColunas disponíveis:")
        for col in df.columns:
            print(f"  - {col}")
        
        # Mostrar primeiras linhas
        print(f"\nPrimeiras 5 linhas:")
        print(df.head())
        
        # ============================================
        # ANÁLISE 1: PREÇOS UNITÁRIOS (Unit_Price)
        # ============================================
        print("\n" + "="*60)
        print("ANÁLISE 1: PREÇOS UNITÁRIOS (Unit_Price)")
        print("="*60)
        
        if 'Unit_Price' in df.columns:
            precos_array = df['Unit_Price'].values
            
            print(f"Total de preços analisados: {len(precos_array)}")
            print(f"Preço mínimo: ${precos_array.min():.2f}")
            print(f"Preço máximo: ${precos_array.max():.2f}")
            
            # Chamar a função de cálculo
            medidas_precos = calcular_medidas_descritivas(precos_array)
            
            # Chamar a função de visualização
            if medidas_precos:
                gerar_painel_boxplot(
                    precos_array, 
                    medidas_precos, 
                    titulo_boxplot='Boxplot dos Preços Unitários (Unit_Price)', 
                    caminho_salvar='Boxplot_Precos_Unitarios.png'
                )
        else:
            print("ERRO: Coluna 'Unit_Price' não encontrada no arquivo CSV")
            print("Colunas disponíveis:", df.columns.tolist())
        
        # ============================================
        # ANÁLISE 2: RECEITA TOTAL (Total_Revenue)
        # ============================================
        print("\n" + "="*60)
        print("ANÁLISE 2: RECEITA TOTAL (Total_Revenue)")
        print("="*60)
        
        if 'Total_Revenue' in df.columns:
            receita_array = df['Total_Revenue'].values
            
            print(f"Total de transações analisadas: {len(receita_array)}")
            print(f"Receita mínima: ${receita_array.min():.2f}")
            print(f"Receita máxima: ${receita_array.max():.2f}")
            print(f"Receita total: ${receita_array.sum():.2f}")
            
            # Chamar a função de cálculo
            medidas_receita = calcular_medidas_descritivas(receita_array)
            
            # Chamar a função de visualização
            if medidas_receita:
                gerar_painel_boxplot(
                    receita_array, 
                    medidas_receita, 
                    titulo_boxplot='Boxplot da Receita Total (Total_Revenue)', 
                    caminho_salvar='Boxplot_Receita_Total.png'
                )
        else:
            print("ERRO: Coluna 'Total_Revenue' não encontrada")
        
        # ============================================
        # ANÁLISE 3: UNIDADES VENDIDAS (Units_Sold)
        # ============================================
        print("\n" + "="*60)
        print("ANÁLISE 3: UNIDADES VENDIDAS (Units_Sold)")
        print("="*60)
        
        if 'Units_Sold' in df.columns:
            unidades_array = df['Units_Sold'].values
            
            print(f"Total de transações analisadas: {len(unidades_array)}")
            print(f"Mínimo de unidades: {unidades_array.min()}")
            print(f"Máximo de unidades: {unidades_array.max()}")
            print(f"Total de unidades vendidas: {unidades_array.sum()}")
            
            # Chamar a função de cálculo
            medidas_unidades = calcular_medidas_descritivas(unidades_array)
            
            # Chamar a função de visualização
            if medidas_unidades:
                gerar_painel_boxplot(
                    unidades_array, 
                    medidas_unidades, 
                    titulo_boxplot='Boxplot das Unidades Vendidas (Units_Sold)', 
                    caminho_salvar='Boxplot_Unidades_Vendidas.png'
                )
        else:
            print("ERRO: Coluna 'Units_Sold' não encontrada")
        
        # ============================================
        # ANÁLISE POR CATEGORIA
        # ============================================
        print("\n" + "="*60)
        print("ANÁLISE POR CATEGORIA DE PRODUTO")
        print("="*60)
        
        if 'Product_Category' in df.columns:
            categorias = df['Product_Category'].unique()
            print(f"Categorias encontradas: {categorias}")
            
            for categoria in categorias:
                print(f"\n{'-'*40}")
                print(f"CATEGORIA: {categoria}")
                print(f"{'-'*40}")
                
                # Filtrar dados da categoria
                dados_categoria = df[df['Product_Category'] == categoria]
                
                if 'Unit_Price' in df.columns:
                    precos_categoria = dados_categoria['Unit_Price'].values
                    
                    if len(precos_categoria) > 0:
                        print(f"Transações nesta categoria: {len(precos_categoria)}")
                        
                        # Calcular medidas
                        medidas_categoria = calcular_medidas_descritivas(precos_categoria)
                        
                        if medidas_categoria:
                            gerar_painel_boxplot(
                                precos_categoria,
                                medidas_categoria,
                                titulo_boxplot=f'Boxplot - {categoria} (Preços)',
                                caminho_salvar=f'Boxplot_{categoria.replace(" ", "_")}.png'
                            )
        
    except FileNotFoundError:
        print(f"ERRO: O arquivo {caminho_csv} não foi encontrado.")
        print("Coloque o arquivo 'Online_Sales_Data.csv' na mesma pasta deste script.")
        print("\nVocê pode:")
        print("1. Copiar o arquivo CSV para esta pasta")
        print("2. Ou alterar o caminho no código")
        
    except Exception as e:
        print(f"ERRO: Ocorreu um erro: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()