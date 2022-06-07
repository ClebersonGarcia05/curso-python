""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final mostre: 

A) Quantas pessoas tem mais de 18 anos 

B) Quantos homens foram cadastrados 

C) Quantas mulheres tem menos de 20 anos.  """

import os


cont = 0
qtdh = 0
qtdm = 0
while True:
    idade = int(input('Informe a idade da pessoa: '))
    sexo = str(input('Informe o sexo da pessoa [M/F]: ')).strip().lower()[0]
    while sexo[0] != 'm' and sexo[0] != 'f':
        print('Opção inválida, tente novamente!\n')
        sexo = str(input('Informe o sexo da pessoa: [M/F]')).strip().lower()[0]
    if idade >= 18:
        cont += 1
    if sexo[0] == 'm':
        qtdh += 1
    elif sexo[0] == 'f' and idade < 20:
        qtdm += 1
    print('\nPessoa cadastrada com sucesso!\n')
    continuar = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
    else:
        os.system('cls')

print(f'A quantidade de pessoas maiores de 18 anos é: {cont}')
print(f'A quantidade de homens cadastrados é de: {qtdh}')
print(f'A quantidade de mulheres com menos de 20 anos é: {qtdm}')