""" Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma 
pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições."""

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional'
    else:
        return f'Com {idade} anos o voto é obrigatório'

print(voto(int(input('Ano de nascimento: '))))