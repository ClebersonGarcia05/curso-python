'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date

atual = date.today().year
maior = 0
menor = 0
for i in range(7):
    ano = int(input(f'Digite o {i+1}º ano de nascimento: '))

    idade = atual - ano

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'''A quantidade de pessoas que são maiores de idade é: {maior}
A quantidade de pessoas que são menores de idade é: {menor} ''')