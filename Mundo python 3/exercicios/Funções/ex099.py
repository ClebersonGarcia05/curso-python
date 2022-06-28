""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior. """

from time import sleep

from numpy import empty


def maior(* num):
    cont = maior =0
    print('Analisando os valores passados...')
    for v in num:
        sleep(0.5)
        cont += 1
        print(f'{v} ', end='', flush='False')
        if v >= maior:
            maior = v
    print(f'Foi informado {cont} valores ao todo.')
    print(f'O maior número é {maior}')
    print()


maior(2, 4, 5, 67, 9, 5, 26, 165)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()