""" Crie um programa que faça o computador jogar jokenpô com você. """

from random import randint
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)

print("""\n0 - Pedra
1 - Papel
2 - Tesoura """)

esc = int(input('\nEscolha uma opção: '))

if esc < 0 or esc > 2:
    print('\n\033[31mOpção inválida tente novamente.\033[m')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\n')
print('-=' * 27)
print(f'Você escolheu {lista[esc]} e o computador escolheu {lista[comp]}')
print('-=' * 27)

if comp == 0: #COMPUTADOR JOGOU PEDRA
    if esc == 0:
        print('\n\033[33mEmpate!\033[m')
    elif esc == 1:
        print('\n\033[32mVocê venceu! Parabéns.\033[m')
    elif esc == 2:
        print('\n\033[31mO computador venceu! Tente novamente.\033[m')
    else:
        print('\n\033[31mOpção inválida tente novamente.\033[m')
elif comp == 1:#COMPUTADOR JOGOU PAPEL
    if esc == 0:
        print('\n\033[31mO computador venceu! Tente novamente.\033[m')
    elif esc == 1:
        print('\n\033[33mEmpate!\033[m')
    elif esc == 2:
        print('\n\033[32mVocê venceu! Parabéns.\033[m')
    else:
        print('\n\033[31mOpção inválida tente novamente.\033[m')
else: #COMPUTADOR JOGOU TESOURA
    if esc == 0:
        print('\n\033[32mVocê venceu! Parabéns.\033[m')
    elif esc == 1:
        print('\n\033[31mO computador venceu! Tente novamente.\033[m')
    elif esc == 2:
        print('\n\033[33mEmpate!\033[m')
    else:
        print('\n\033[31mOpção inválida tente novamente.\033[m')
