""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acondom com sua idade:

Se ele ainda vai se alistar ao serviço militar

Se já é hora de se alistar

Se já passou do tempo do alistamento

Seu programa também deverá mostar o tempo que falta ou que passou o prazo """

from datetime import datetime


ano = int(input('Qual o ano de seu ano de nascimento?'))
atual = datetime.today().year
idade = atual - ano

print(f'\nQuem nasceu em {ano} tem {idade} anos em {atual} ')

if idade < 17:
    print(f'\nVocê terá que se alistar no serviço militar daqui a {18 - idade} anos!')
    print(f'E seu ano de alistamento será em {ano + 18}')
elif idade >= 17 and idade <=18:
    print('Já é hora de se alistar no serviço militar!')
else:
    print(f'Era para você ter se alistado no serviço militar a {idade - 18} anos atrás!')
    print(f'E seu ano de alistamento foi em {ano + 18}')