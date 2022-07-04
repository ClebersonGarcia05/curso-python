""" Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta. """

from random import randint

jogos = int(input('Digite quantos jogos quer gerar: '))
lista = []
for i in range(jogos):
    for j in range(6):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    print(f'{i+1}º sorteio : {lista}')
    lista.clear()