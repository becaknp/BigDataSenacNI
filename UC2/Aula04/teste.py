import pandas as pd
import mysql.connector

def obter_dados_do_banco(query):
 # código da função da aula anterior
    query_clientes = "SELECT * FROM clientes"
    df_clientes = pd.DataFrame(obter_dados_do_banco(query_clientes), columns=['id_cliente',
    'nome', 'email'])
    print(df_clientes)
    #Crie outro DataFrame a partir de um arquivo CSV ou Excel com os pedidos.
    df_pedidos = pd.read_csv('pedidos.csv')
    print(df_pedidos)
    #Agora, vamos relacionar os dois DataFrames usando a função merge:
    # Relacionando os DataFrames pela coluna 'id_cliente'
    df_relacionado = pd.merge(df_clientes, df_pedidos, on='id_cliente', how='inner')
    print(df_relacionado)