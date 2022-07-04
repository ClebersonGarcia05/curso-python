'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo'''

num = int(input('Digite um número: '))

cont =0
for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[33m{i}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[31m{i}\033[m', end=' ')
print(f'\nO número {num} foi dividido {cont} vezes')
if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')

#OU

""" 
for i in range(2, num):
    if num % i == 0:
        print(f'Multiplo de {i}')
        cont +=1
if cont == 0:
    print('É primo')
else: 
    print(f'Não é primo, pois tem {cont} múltilos acima de 2 e abaixo de {num}') """