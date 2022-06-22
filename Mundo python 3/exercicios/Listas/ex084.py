""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves."""

pessoas = [[], []]
while True:
    pessoas[0].append(str(input('Nome: ')))
    pessoas[1].append(float(input('Peso: ')))
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        print('Digite uma opção válida!')
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foi {len(pessoas[0])} pessoas cadastradas.')
print(f'As pessoas mais pesadas são ', end='')
for pos, v in enumerate(pessoas[1]):
    if v >= max(pessoas[1]):
        print(f'{pessoas[0][pos]}, ', end='')
print(f'pesando {max(pessoas[1])}Kg. ')
print(f'As pessoas mais leves são ', end='')
for pos, v in enumerate(pessoas[1]):
    if v <= min(pessoas[1]):
        print(f'{pessoas[0][pos]}, ', end='')
print(f'pesando {min(pessoas[1])}Kg. ')