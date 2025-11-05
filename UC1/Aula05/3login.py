# ===============================
# 3. Tentativa de Login e Senha
# ===============================
print("\n=== Sistema de Login ===")
usuario_correto = "admin"
senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    try:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso!")
            break
        else:
            tentativas -= 1
            print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if tentativas == 0:
    print("Bloqueado! Número máximo de tentativas atingido.")