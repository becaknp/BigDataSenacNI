#### Desafio 1: Ordenação de Três Números ####

# Recebidos 3 números inteiros, crie um programa que os mostre ordenados em ordem crescente.
# Dica: Este desafio exige que você use estruturas if aninhadas ou uma série de testes
# usando operadores de comparação para determinar qual número é o menor, o do
# meio e o maior.

a=int(input('Informe seu primeiro número: '))
b=int(input('Informe seu segundo número: '))
c=int(input('Informe seu terceiro número: '))

primeiro=None
segundo=None
terceiro=None

if a<b and a<c:  # abc ou acb
    primeiro=a   
    if b<c:      # abc
        segundo=b
        terceiro=c
    else:        # acb
        segundo=c
        terceiro=b
elif b<a and b<c:  # bac ou bca
    primeiro=b
    if a<c:        # bac
        segundo=a
        terceiro=c
    else:          # bca
        segundo=c
        terceiro=a
elif c<a and c<b: # cab ou cba
    primeiro=c
    if a<b:   # cab
        segundo=a
        terceiro=b
    else:     # cba
        segundo=b
        terceiro=a
else:
    print('Erro na informação dos números.')

print(f'Ordem:{primeiro},{segundo},{terceiro}')
