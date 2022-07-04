from random import randint

num = randint(0, 5)

escolhido = int(input('Tente adivinhar o número que o pc escolheu entre 0 e 5: '))

if escolhido == num:
    print('Você acertou!!!')
else:
    print(f'O número sorteado foi {num} e você escolheu {escolhido}')
    print('Tente novamente!!!')