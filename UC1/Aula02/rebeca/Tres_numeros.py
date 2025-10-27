num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#Testa se num1 é o menor de todos
if num1 < num2 and num1 < num3:
    print(f'O menor número é: {num1}')
#Senão, testa se num2 é o menor de todos
elif num2 < num1 and num2 < num3:
    print(f'O menor número é: {num2}')
#Senão, o num3 é o menor
else:
    print(f'O menor número é: {num3}')

#Testa se num1 é o do meio
if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print(f'O número do meio é: {num1}')
#Senão, testa se num2 é o do meio
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print(f'O número do meio é: {num2}')
#Senão, o num3 é o do meio
else:
    print(f'O número do meio é: {num3}')

#Testa se num1 é o maior de todos
if num1 > num2 and num1 > num3:
    print(f'O maior número é: {num1}')
#Senão, testa se num2 é o maior de todos
elif num2 > num1 and num2 > num3:
    print(f'O maior número é: {num2}')
#Senão, o num3 é o maior
else:
    print(f'O maior número é: {num3}')

print('Fim do programa.')

