""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um 
dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas

B) A média de idade do grupo

C) Uma lista com todas as mulheres

D) Uma lista com todas as pessoas com idade acima da média"""

dicio = dict()
lista = list()
mulheres = list()
média = list()
nomes = list()
cont = 0
s = 0
while True:
    dicio['nome'] = str(input('Digite seu nome: ')).strip().upper()
    dicio['sexo'] = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    while dicio['sexo'] not in 'MF':
        dicio['sexo'] = str(input('Opção inválida, digite seu sexo [M/F]: ')).strip().upper()[0]
    dicio['idade'] = int(input('Digite sua idade: '))
    s += dicio['idade']
    cont += 1
    if dicio['sexo'] == 'F':
        mulheres.append(dicio['nome'])
    lista.append(dicio.copy())
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while r not in 'SN':
        r = str(input('Opção inválida, quer continuar? [S/N]: ')).strip().upper()
    if r == 'N':
        break
media = s / cont
print('-=' * 30)
print(f'Foram {len(lista)} pessoas cadastradas!')
print()
print(f'A média de idade entre os cadastrados é: {media:.2f}')
print()
print(f'Todas as mulheres cadastradas foram: {mulheres}')
print()
print(f'Os nomes das pessoas com idade acima da média é:')
for p in lista:
    if p['idade']  >= media:
        print()
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('-=' * 30)