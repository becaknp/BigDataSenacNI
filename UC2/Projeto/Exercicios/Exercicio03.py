import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="sales_online"
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

# Usando a função
query_produtos = "SELECT * FROM vendas WHERE Total_Revenue > 500"
dados_filtrados = obter_dados_do_banco(query_produtos)

if dados_filtrados:
    for produto in dados_filtrados:
        print(produto)

'''
4. Crie uma função para consultar a tabela;
5. Execute consultas para responder às seguintes perguntas, imprimindo os resultados:
○ Liste o nome de todos os elementos;.
○ Encontre o nome e algum valor quantitativo ligado a esses elementos;
○ Conte quantos elementos possuem algum filtro de categoria.'''