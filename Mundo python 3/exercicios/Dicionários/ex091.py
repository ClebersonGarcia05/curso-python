""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. """

from operator import itemgetter
from random import randint
from time import sleep

jogos = {}
lista = []
for i in range(4):
    jogos[f'Jogador {i+1}'] = randint(1,6)
for k, v in jogos.items():
    print(f'O jogador {k} tirou o número: {v}')
    sleep(1)
lista = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('\nRANKING DOS JOGADORES: ')
for i, v in enumerate(lista):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)