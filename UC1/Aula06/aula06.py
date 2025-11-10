#### LISTAS #### List

# lista02_nopet=[
#     'Lavar louça',
#     'Ir ao Mercado',
#     'Lavar Banheiro',
#     'Tirar poeira',
#     'Lavar quintal',]
# lista02_pets=lista02_nopet.copy() #variavel nova com copia da lista ja existente
# lista02_pets.append('Dar banho no doguinho') #adicionar elemento 
# lista02_pets.append('Limpar areia do gato') #Adicionar um elemento na lista

# lista02_pets.insert(5,'Ir ao vet') #o numero escolhe o indice que ele vai ser inserido
# '''no insert você pode escolher aonde vai inserir'''
# #não tem como colocar 2 elementos em uma append
# # lista02.pop() #remover um elemento na lista
# lista02_pets.remove('Ir ao vet')
# print(lista02_nopet, lista02_pets)
# print('*'*30) #imprimir esse simbolo 30 vezes, tem que colocar * fora das aspas pra indicar quantidade
# # print(lista02_pets)
# # print(lista02_pets[1][6:13]) #Caso queira imprimir apenas uma palavra em especifico, primeiro puxa o elemento, nesse caso 1, e depois cita a palvra, ir ao mercado são 12 caracteres, nesse caso ficaria 1(puxar a frase) depois 6:12(6 ao 12)que é a palavra toda
# # print(lista02_pets[1][6:]) #tudo depois de mercado no indice 1
# # print(lista02_pets[1][:6]) #tudo antes do mercado no indie 1
# # print(lista02_pets[1][6:]), lista02[4][6:] #pegar 2 palavras de indices diferentes

# #remover um elemento especifico na lista
# '''Append e pop adicioanr/remove sempre o ultimo, ja o insert e remove você escolhe o que quer remover e adicionar,
# você pode dizer onde está pra ele remover/add'''
# #lembrete que a contagem começa por 0
# # pilha e fila conceitos pesquisar


#### TUPLAS #### tuple

# pares=(40,20,2,18,14,34,96,30,20,58)
# print(pares[3])
# print(pares[3:]) #do indice 3 em diante
# print(pares[3:8]) #do indice 3 as 8 (ele descarta sempre o ultimo numero igual lista)
# print(len(pares)) #len me diz a quantidade de elementos 
# pares=pares+(44,) #adicionar o numero na tupla, é como se fosse uma variavel 'nova' mais a variavel e o que for adicionado
# print(pares)
# #conversão de int/str pra list e dps list pra tuple
# lista_pares=list(pares)
# print(lista_pares)
# lista_pares.append(102)
# lista_pares.sort() #organizar os elementos em uma lista usar o sort
# lista_pares=tuple(lista_pares)
# print(lista_pares)

#### SETS #### set

# impares={33,5,17,11,27,11,71,79,99,15}
# nmrs={22,22,22,22,22,33,33,33,33,44,44,44,55,55,66,66,4,4,4,5,5,5} #ele nao repete o mesmo numero
# # print(impares)
# # print(type(impares))
# # print(nmrs)
# impares_02={11,3,23,83,15,73}
# uniao=impares.union(impares_02) #une os sets
# intersecao=impares.intersection(impares_02) #mostra so os numeros que em ambas os sets tem
# print(intersecao)
# print(uniao)

#### DICIONÁRIOS #### dict
#json
filme={
    'nome':'V for Vendetta',
    'ano': 2005,
    'genero':'Ação', #Thriller/Drama
    'faixa_etaria':16
}
print(filme)
print(type(filme))
print((filme['ano'])) #pra imprimir o tipo de chave dentro da variavel dict
print((filme['nome']))
print((filme['genero']))
print((filme['faixa_etaria']))

print(filme.keys()) #ver as chaves dentro da variavl dict
print(filme.values()) #valores guardados nas chaves
print(len(filme)) #quantidade de chaves

filme['duracao']= '130min' #pra adicionar uma chave com um novo valor
filme['genero']= 'Thriller/Drama' #trocar algum valor dentro da chave
filme.pop('duracao') #remove pela chave
print(filme)