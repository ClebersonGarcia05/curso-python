""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date
from time import sleep

cad = {}
cad['nome'] = str(input('Digite seu nome: '))
nasc = int(input('Digite seu ano de nascimento: '))
cad['carteira'] = int(input('Digite o número da carteira [0 se não tiver]: '))
cad['idade'] = date.today().year - nasc
if cad['carteira'] != 0:
    cad['contratação'] = int(input('Digite o ano de contratação: '))
    cad['salario'] = float(input('Digite o salario: R$'))
    cad['aposentar'] = cad['idade'] + ((cad['contratação'] + 35) - date.today().year)
else:
    cad['carteira'] = 'Não tem'
print()
for k, v in cad.items():
    print(f'{k} tem o valor {v}')
    sleep(1)