""" A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

até 9 anos: mirim
até 14 anos: Infantil 
até 19 anos: Junior
até 20 anos: Sênior
Acima: Master"""

from datetime import datetime


ano = int(input('Qual seu ano de nascimento? '))

idade = datetime.today().year - ano

if idade <= 9:
    print('Sua categoria é: MIRIM')
elif idade <= 14:
    print('Sua categoria é: INFANTIL')
elif idade <= 19:
    print('Sua categoria é: JUNIOR')
elif idade <= 20:
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')