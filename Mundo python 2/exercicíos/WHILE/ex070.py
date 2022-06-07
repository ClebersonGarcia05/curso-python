""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
continuar. No final, mostre: 

A) Qual é o total gasto na compra 

B) Quantos produtos custam mais de R$1000,00 

C) Qual é o nome do produto mais barato """

cont = 0
total = 0
mp = 0
n = ''
andador = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip().lower()
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    andador += 1
    if andador == 1:
        mp = preco
        n = nome
    if preco > 1000:
         cont += 1
    elif preco <= mp:
        n = nome
        mp = preco
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'O total gasto na compra é de: R${total}.')
print(f'{cont} produto(s) custam mais de R$1000,00.')
print(f'O produto mais barato é: {n} custando {mp}')