lista01=[100,20,43,23,675,23,12,55]
#           [0]    [1] [2]  [3] ...
for i in lista01:
    print(i,':',type(i))

print(lista01[-1][2])


## TUPLAS ###

pares=(40,20,2,18,14,34,96,30,20,58)
print(pares[3])
print(pares[3:])
print(pares[3:8])
print(len(pares))
pares=pares+(44,)
print(pares)
lista_pares=list(pares)
print(lista_pares)
lista_pares.append(102)
lista_pares.sort()
lista_pares=tuple(lista_pares)
print(lista_pares)

### SETS ###
impares={33,5,17,11,27,11,71,79,99,15}
print(impares)
print(type(impares))
impares_02={11,3,23,83,15,73}
intersecao=impares.intersection(impares_02)
print(intersecao)

### DICIONÁRIOS ###

filme={
    'nome':'V for Vendetta',
    'ano': 2005,
    'genero':'Ação', #Thriller/Drama
    'faixa_etaria':16
}
print(filme)
print(type(filme))

print(filme.keys())
print(filme.values())
print(len(filme))

filme['duracao']='130min'
filme['genero']='Thriller/Drama'
filme['genero']=None
print(filme)

def origem_produtos():
    print("--- 4. CÓDIGO DE ORIGEM (MATCH/CASE) ---")
    try:
        codigo = int(input("Digite o código de origem (inteiro, ex: 7, 15 ou 90): "))
        
        # ESTRUTURA MATCH/CASE
        match codigo:
            case 1:
                procedencia = "Sul"
            case 2:
                procedencia = "Norte"
            case 3:
                procedencia = "Leste"
            case 4:
                procedencia = "Oeste"
            case 5 | 6:
                procedencia = "Nordeste"
            # Faixa com Condição (Guard: 'if')
            case n if 7 <= n <= 9:
                procedencia = "Sudeste"
            case 10:
                procedencia = "Centro-Oeste"
            case 11:
                procedencia = "Nordeste"
            # Caso Padrão (Default)
            case _:
                procedencia = "Importado"

        print(f"Resultado:\n  Código {codigo} -> Procedência: {procedencia}\n")
        
    except ValueError:
        print("ERRO: Digite um número inteiro válido.")

print(origem_produtos)





