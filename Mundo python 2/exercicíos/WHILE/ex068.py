""" Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder
mostrando o total de vitórias consecultivas que ele conquistou no final do jogo """

import os
from random import randint

cont = 0
while True:
    print('='*20)
    print('Jogo do par ou impar')
    print('='*20)
    jogador = str(input('Você escolhe par ou impar? ')).strip().lower()
    while jogador != 'par' and jogador != 'impar' and jogador[0] != 'p' and jogador[0] != 'i':
        print('Opção inválida, digite novamente!')
        jogador = str(input('Você escolhe par ou impar? ')).strip().lower()
    num = int(input('Difite um número de 0 a 10: '))
    while num < 0 or num > 10:
        print('Escolha um número válido!')
        num = int(input('Difite um número de 0 a 10: '))
    comp = randint(0, 10)
    soma = num + comp
    print(f'\nO computador escolheu o número {comp} e você {num} e a soma entre eles é: {soma}')
    if soma %2 == 0:
        print('\nO número é par.')
        if jogador == 'par' or jogador[0] == 'p':
            print('\nVocê venceu do computador!')
            cont += 1
        else:
            print('\nO computador venceu! Tente novamente.')
            break
    else:
        print('\nO número é impar.')
        if jogador == 'impar' or jogador[0] == 'i':
            print('\nVocê venceu do computador!')
            cont += 1
        else:
            print('\nO computador venceu! Tente novamente.')
            break
    continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()
    if continuar[0] == 'N':
        break
    else:
        os.system('cls')
        continue
print(f'Você ganhou {cont} vezes do computador!')