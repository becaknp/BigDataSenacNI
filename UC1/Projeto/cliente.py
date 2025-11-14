# cliente.py

import random
import time
from dados import cardapio, pedidos_abertos

def format_price(valor):
    return f"R${int(valor)}" if float(valor).is_integer() else f"R${valor:.2f}"

def total_parcial_temp(lista):
    return sum(preco * qtd for _, preco, qtd in lista)

def mostrar_cardapio():
    print("-" * 40)
    print("------------ CARDÁPIO ------------")
    print("-" * 40)
    for categoria, itens in cardapio.items():
        print(f"\n{categoria}:")
        indice = 1
        for nome, preco, desc in itens:
            print(f"{indice} - {nome} - {format_price(preco)} | {desc}")
            indice += 1
        print("-" * 40)

def gerar_nota_fiscal(cliente, mesa, itens, total, metodo_pagamento, parcelas=None):
    nf_numero = random.randint(100000, 999999)
    
    print("\n" + "=" * 60)
    print("NOTA FISCAL - RESTAURANTE TANOSHIMI")
    print("=" * 60)
    print(f"NF: {nf_numero}")
    print(f"Data: 2025-11-14 14:23:01")
    print(f"Estabelecimento: Restaurante Japonês Tanoshimi")
    print(f"Localização: Av. Lúcio Costa – Barra da Tijuca, RJ")
    print(f"CNPJ: 12.345.678/0001-90")
    print("-" * 50)
    print(f"Cliente: {cliente}")
    print(f"Mesa: {mesa}")
    print("-" * 50)
    
    print("ITENS:")
    for nome, preco, qtd in itens:
        subtotal = preco * qtd
        print(f"{nome} ({qtd}x) - R${preco:.2f} cada - Total: R${subtotal:.2f}")
    
    print("-" * 50)
    print(f"TOTAL: R$ {total:.2f}")
    
    # Mostra se foi parcelado
    if parcelas and parcelas > 1:
        print(f"Método: {metodo_pagamento} ({parcelas}x de R$ {total/parcelas:.2f})")
    else:
        print(f"Método: {metodo_pagamento}")
    
    print("-" * 50)
    print("Obrigado pela preferência!")
    print("Sistema desenvolvido por: Rebeca Knupp da Silva")
    print("=" * 60)

def fazer_pedido(cliente, mesa):
    itens_temp = []
    mostrar_cardapio()

    while True:
        print("\nDigite uma categoria do cardápio para começar o seu pedido")
        print("Ou essas outras opções (resumo do pedido / remover item / enviar pedido / voltar)")
        categoria = input("-> ").strip().lower()

        if categoria == "voltar":
            return itens_temp

        elif categoria == "resumo do pedido" or categoria == "resumo":
            if not itens_temp:
                print("Nenhum item adicionado ainda!")
            else:
                print("-" * 40)
                for i in range(len(itens_temp)):
                    nome, preco, qtd = itens_temp[i]
                    print(f"{i + 1} - {nome} ({qtd}x)")
                print(f"Total parcial: {format_price(total_parcial_temp(itens_temp))}")
                print("-" * 40)

        elif categoria == "remover item" or categoria == "remover":
            if not itens_temp:
                print("Nenhum item para remover!")
            else:
                for i in range(len(itens_temp)):
                    nome, preco, qtd = itens_temp[i]
                    print(f"{i + 1} - {nome} ({qtd}x)")

                try:
                    remover = int(input("Número do item: "))
                except ValueError:
                    print("Entrada inválida! Digite um número.")
                else:
                    if remover < 1 or remover > len(itens_temp):
                        print("Esse número não existe.")
                    else:
                        item_removido = itens_temp.pop(remover - 1)
                        print(f"Item {item_removido[0]} removido!")

        elif categoria == "enviar pedido" or categoria == "enviar":
            if not itens_temp:
                print("Nenhum item no pedido!")
            else:
                print("\nConfirme seu pedido:")
                total_final = total_parcial_temp(itens_temp)
                for nome, preco, qtd in itens_temp:
                    print(f"{nome} ({qtd}x)")
                print(f"Total: {format_price(total_final)}")

                if input("Enviar? (1-Sim / 2-Não): ") == "1":
                    id_pedido = random.randint(10000, 99999)
                    pedidos_abertos.append({
                        "id": id_pedido,
                        "cliente": cliente,
                        "mesa": mesa,
                        "itens": itens_temp[:],
                        "entregue": False
                    })
                    print("Pedido enviado para cozinha!")
                    print(f"Número do seu pedido: {id_pedido}")
                    time.sleep(1)
                    return itens_temp

        else:
            # Parte de Adicionar item(quando não é nenhum dos comandos especiais)
            itens_encontrados = None
            for cat in cardapio:
                if categoria == cat.lower():
                    itens_encontrados = cardapio[cat]
                    break

            if itens_encontrados is None:
                print("Categoria inválida!")
            else:
                try:
                    idx = int(input("Número do item: ")) - 1
                except ValueError:
                    print("Digite apenas números!")
                else:
                    if idx < 0 or idx >= len(itens_encontrados):
                        print("Esse item não existe!")
                    else:
                        try:
                            qtd = int(input("Quantidade: "))
                        except ValueError:
                            print("Digite apenas números!")
                        else:
                            nome, preco, _ = itens_encontrados[idx]
                            itens_temp.append((nome, preco, qtd))
                            subtotal = preco * qtd
                            total_atual = total_parcial_temp(itens_temp)
                            print(f"\nItem adicionado: {nome} ({qtd}x) - R${subtotal:.2f}")
                            print(f"Total parcial: R${total_atual:.2f}")

def encontrar_pedidos_mesa(mesa):
    """Encontra todos os pedidos de uma mesa específica"""
    pedidos_mesa = []
    for pedido in pedidos_abertos:
        if pedido["mesa"] == mesa and pedido.get("entregue", False):
            pedidos_mesa.append(pedido)
    return pedidos_mesa

def pagar():
    informacoes_corretas = False
    
    while not informacoes_corretas:
        print("\n--- PAGAMENTO ---")
        
        # Cliente informa a mesa
        try:
            mesa = int(input("Informe o número da sua mesa: "))
        except ValueError:
            print("Número de mesa inválido! Digite apenas números.")
        else:
            # Encontrar pedidos da mesa que ja foram entregues
            pedidos_mesa = encontrar_pedidos_mesa(mesa)
            
            if not pedidos_mesa:
                print("Mesa não encontrada ou nenhum pedido entregue para esta mesa. Digite novamente.")
            else:
                # Calcular total antes para mostrar na confirmação
                total_confirmacao = 0
                for pedido in pedidos_mesa:
                    total_confirmacao += sum(preco * qtd for nome, preco, qtd in pedido["itens"])
                
                # Mostrar confirmação com total
                print("\nAntes de pagar confirme se as informações estão corretas:")
                print("-" * 50)
                
                for pedido in pedidos_mesa:
                    print(f"Nome do cliente: {pedido['cliente']}")
                    print(f"Mesa: {pedido['mesa']}")
                    print(f"Pedido:")
                    for nome, preco, qtd in pedido["itens"]:
                        print(f"  - {nome} ({qtd}x)")
                    print("-" * 50)
                
                print(f"TOTAL: {format_price(total_confirmacao)}")
                print("-" * 50)
                
                # Confirmação final
                confirmar = input("As informações estão corretas? (1-Sim / 2-Não): ")
                if confirmar == "1":
                    informacoes_corretas = True
                    
                    # Calcular total
                    total = total_confirmacao
                    
                    print(f"\nTOTAL A PAGAR: {format_price(total)}")

                    # Sistema de pagamento
                    parcelas = None
                    pagamento_valido = False
                    while not pagamento_valido:
                        print("\nMétodos de pagamento:")
                        print("1 - Pix")
                        print("2 - Cartão") 
                        print("3 - Dinheiro")
                        
                        opcao = input("Escolha o método (1/2/3): ").strip()
                        
                        if opcao == "1":
                            metodo_formatado = "Pix"
                            pagamento_valido = True
                        elif opcao == "2":
                            print("\nOpções de parcelamento:")
                            print("1x - R$ {:.2f}".format(total))
                            print("2x - R$ {:.2f}".format(total / 2))
                            print("3x - R$ {:.2f}".format(total / 3))
                            
                            try:
                                parcelas = int(input("Digite o número de parcelas (1/2/3): "))
                                if parcelas not in [1, 2, 3]:
                                    print("Número de parcelas inválido! Usando 1 parcela.")
                                    parcelas = 1
                            except ValueError:
                                print("Entrada inválida! Usando 1 parcela.")
                                parcelas = 1
                                
                            metodo_formatado = "Cartão"
                            pagamento_valido = True
                        elif opcao == "3":
                            metodo_formatado = "Dinheiro"
                            pagamento_valido = True
                        else:
                            print("Opção inválida! Escolha 1, 2 ou 3.")

                    print("Pagamento aprovado!")
                    
                    # Gerar nota fiscal para cada pedido
                    for pedido in pedidos_mesa:
                        pedido_total = sum(preco * qtd for nome, preco, qtd in pedido["itens"])
                        gerar_nota_fiscal(pedido["cliente"], pedido["mesa"], pedido["itens"], pedido_total, metodo_formatado, parcelas)
                    
                    # Remove os pedidos da lista de abertos
                    for pedido in pedidos_mesa:
                        pedidos_abertos.remove(pedido)
                    
                    print("Obrigado e volte sempre!")
                    time.sleep(2)

def sistema_cliente(): # Função principal do cliente
    print("-" * 40)
    print("Seja bem-vindo ao Tanoshimi!")
    print("-" * 40)

    # Verifica se já tem o pedido pronto para pagar
    cliente_existente = None
    mesa_existente = None
    
    for pedido in pedidos_abertos:
        if pedido.get("entregue", False):
            cliente_existente = pedido["cliente"]
            mesa_existente = pedido["mesa"]
            break
    
    if cliente_existente:
        print(f"{cliente_existente}, Mesa {mesa_existente}.")
        print("Seu pedido está pronto para pagamento!")
        pagar()
        return
    else:
        # Se não tem pedido pronto,faz novo pedido
        cliente = input("Seu nome: ")
        mesa = 1  # mesa fixa para simplificar
        print(f"Cliente: {cliente} - Mesa {mesa}")
        
        # Fazer pedido
        itens = fazer_pedido(cliente, mesa)
        
        if itens:
            print("\nPedido realizado com sucesso!")
            print("Aguarde o garçom entregar seu pedido.")
            print("Volte ao sistema depois para pagar.")

if __name__ == "__main__":
    sistema_cliente()