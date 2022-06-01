'''Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiusculas

O nome com todas as letris minusculas

Quantas letras ao todo (sem considerar espaços)

Quantas letras tem o primeiro nome'''

nome = str(input('Qual o seu nome completo? ')).strip()
separa = nome.split()

#print(f'Quantidade de letras do primeiro nome{nome.find(' ')}')

print(f"""Seu nome em maiusculas: {nome.upper()}\n
Seu nome em minusculas: {nome.lower()}\n
Quantidade de letras sem espaço: {len(nome.replace(" ", ""))}\n
Quantidade de letras no primeiro nome: {len(separa[0])}""")