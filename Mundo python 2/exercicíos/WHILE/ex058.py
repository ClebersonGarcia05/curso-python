""" Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
Só que agora o jogador vai tenta adivinhar até acertar mostrando no final quantas  tentativas foram necessárias
para vencer """

from random import randint

comp = randint(0,10)

esc = int(input('Escolha um número entre 0 e 10: '))
cont = 0

while esc != comp:
    print(f'O computador escolheu o número: {comp}')
    comp = randint(0,10)
    esc = int(input('Escolha um número entre 0 e 10: '))
    cont += 1

print(f'Foram necessárias {cont} tentativas para acertar.')