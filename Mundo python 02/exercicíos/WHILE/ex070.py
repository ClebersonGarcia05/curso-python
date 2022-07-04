""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
continuar. No final, mostre: 

A) Qual é o total gasto na compra 

B) Quantos produtos custam mais de R$1000,00 

C) Qual é o nome do produto mais barato """

cont = total = mp = andador = 0
n = ''
while True:
    nome = str(input('Digite o nome do produto: ')).strip().lower()
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    andador += 1
    if andador == 1 or preco < mp:
        mp = preco
        n = nome
    if preco > 1000:
         cont += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'O total gasto na compra é de: R${total}.')
print(f'{cont} produto(s) custam mais de R$1000,00.')
print(f'O produto mais barato foi {n} que custa R${mp}')