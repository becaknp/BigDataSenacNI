# garcom.py

from dados import pedidos_abertos  # Lista compartilhada com o cliente
import time

# Função única que mostra pedidos E permite dar baixa
def ver_e_gerenciar_pedidos():
    print("\n--- PEDIDOS EM ABERTO ---")

    if not pedidos_abertos:
        print("Nenhum pedido no momento.")
        time.sleep(1)
        return

    # Mostra todos os pedidos
    indice = 1
    for pedido in pedidos_abertos:
        status = "Entregue" if pedido.get("entregue") else "Na Cozinha"
        
        print("-" * 40)
        print(f"Pedido {indice}")
        print(f"ID: {pedido['id']}")
        print(f"Cliente: {pedido['cliente']} - Mesa {pedido['mesa']}")
        print(f"Status: {status}")
        print("Itens:")
        
        # Exibe os itens do pedido
        for nome, preco, qtd in pedido["itens"]:
            print(f" - {nome} ({qtd}x)")
        
        indice += 1

    print("-" * 40)
    
    # Pergunta se quer dar baixa em algum pedido
    print("\nDeseja dar baixa em algum pedido?")
    print("1 - Sim")
    print("2 - Não (Voltar)")
    
    opcao = input("Escolha: ").strip()
    
    if opcao == "1":
        # Lista pedidos para baixa
        print("\nQual pedido deseja dar baixa?")
        
        indice = 1
        for pedido in pedidos_abertos:
            status = "Entregue" if pedido.get("entregue") else "Na Cozinha"
            print(f"{indice} - {pedido['cliente']} | Mesa {pedido['mesa']} | {status}")
            indice += 1
        
        try:
            escolha = int(input("Número do pedido: "))
        except ValueError:
            print("Digite apenas números!")
            return
        
        if escolha < 1 or escolha > len(pedidos_abertos):
            print("Esse pedido não existe!")
            return
        
        pedido = pedidos_abertos[escolha - 1]
        
        # Verifica se já não está entregue
        if pedido.get("entregue"):
            print("Este pedido já foi entregue!")
        else:
            pedido["entregue"] = True  # Marca entrega
            print("Pedido entregue ao cliente!")
        
        time.sleep(1)
    
    elif opcao == "2":
        print("Voltando ao menu...")
    else:
        print("Opção inválida! Voltando ao menu...")

# Menu principal do garçom
def sistema_garcom():
    while True:
        print("\n--- SISTEMA DO GARÇOM ---")
        print("1 - Ver e gerenciar pedidos")
        print("2 - Voltar")
        opc = input("> ")

        if opc == "1":
            ver_e_gerenciar_pedidos()
        elif opc == "2":
            break  # retorna para o menu principal
        else:
            print("Opção inválida!")

# Se rodar direto este arquivo
if __name__ == "__main__":
    sistema_garcom()