""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a 
contagem. Seu programa tem que realizar três contagens atavés da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0 de 2 em 2
C) Uma contagem personalizada """

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush='False')
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush='False')
            sleep(0.5)
            cont -= p
        print('Fim!')
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 43)
print('Agora é sua vez de personalizar a contagem')
print('-' * 43)
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)