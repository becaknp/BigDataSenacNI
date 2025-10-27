n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
n3=float(input('Digite sua terceira nota: '))
n4=float(input('Digite sua quarta nota: '))

media=(n1+n2+n3+n4)/4

print(f'Sua media é:{media}')

if media >7:
    print('Parabéns!Você foi aprovado.')
elif media >= 5:
    print('Infelizmente você está de recuperação.')
else: 
    print('Sua nota não antigiu a media,você foi reprovado')

# control + k + c (comentar tudo)
# control k + u (voltar ao normal)

#Aprovado= Parabéns!Você foi aprovado. media >7
#Recuperacao= Infelizmente você está de recuperação. media > 5 or media < 7
#Reprovacao= Sua nota não antigiu a media,você foi reprovado. media < 5