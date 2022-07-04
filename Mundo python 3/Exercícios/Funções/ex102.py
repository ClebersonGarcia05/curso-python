""" Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela o 
processo de cálculo do fatorial"""

from time import sleep

def fatorial(fat, show='False'):
    """ -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n """

    s = 1
    print(f'Fatorial de {fat}! ', end='')
    for i in range(fat, 0, -1):
        if show == 'True':
            print(i, end='')
            if i > 1: 
                print(f' x ', end='', flush='False')
                sleep(0.5)
            else:
                print(' = ', end='')
        s *= i
    return s

fat, r = int(input('Digite um número: ')), input('Quer show? ').lower().strip()[0]
if r == 's':
    r = 'True'
print(fatorial(fat, r))