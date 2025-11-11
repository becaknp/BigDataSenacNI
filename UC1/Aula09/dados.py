### RPG ###
import random

def rolar_dado(lados):
    return random.randint(1, lados)


input("Pressione Enter para rolar o Ataque (d20)...")
ataque = rolar_dado(20)
print(f"Resultado do Ataque: {ataque}")

input("Pressione Enter para rolar o Dano (d8)...")
dano = rolar_dado(8)
print(f"Resultado do Dano: {dano}")

print("Resumo da Batalha:")
print(f"Ataque: {ataque} | Dano: {dano}")
