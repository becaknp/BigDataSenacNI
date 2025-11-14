# main.py

# Importa menus principais
from cliente import sistema_cliente
from garcom import sistema_garcom

# Menu inicial que acessa cliente ou garçom
def main():
    while True:
        print("-" * 40)
        print("===== MENU PRINCIPAL =====")
        print("1 - Cliente")
        print("2 - Garçom")
        print("3 - Sair")
        opc = input("Escolha: ")

        # Direciona para cada módulo
        if opc == "1":
            sistema_cliente()
        elif opc == "2":
            sistema_garcom()
        elif opc == "3":
            print("Encerrando...")
            break  # finaliza sistema
        else:
            print("Opção inválida!")

# Se rodar direto esse arquivo → inicia menu principal
if __name__ == "__main__":
    main()