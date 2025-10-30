# semana = int(input('Qual dia da semana você quer saber?'))

# if semana == 1:
#     print("Domingo")
# elif semana == 2:
#     print("Segunda-feira")
# elif semana == 3:
#     print("Terça-feira")
# elif semana == 4:
#     print("Quarta-feira")
# elif semana == 5:
#     print("Quinta-feira")
# elif semana == 6:
#     print("Sexta-feira")
# elif semana == 7:
#     print("Sábado")
# else: # O 'else' funciona como o 'default'
#     print("Dia inválido")

try:
    semana = int(input('Qual dia da semana você quer saber?'))
    match semana: 
        case 1:
            print('Domingo')
        case 2:
            print('Segunda')
        case 3:
            print('Terça')
        case 5:
            print('Quarta')
        case 6:
            print('Quinta')
        case 7:
            print('Sexta')
        case 8:
            print('Sábado')
        case _: # O underline ( _ ) funciona como o 'default' ou 'else'
            print("Dia inválido")
except ValueError:
    print('Informação inválida. Por favor informe um número inteiro.') 
