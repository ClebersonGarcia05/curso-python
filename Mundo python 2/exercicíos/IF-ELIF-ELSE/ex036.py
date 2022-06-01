""" escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado"""

valorCasa = float(input('Qual o valor da casa que você quer financiar?'))
salario = float(input('Qual o valor do seu salário?'))
parcela = int(input('Em quantos anos você quer financiar?'))

exceder = salario * 30 / 100

meses = parcela * 12

pres = valorCasa / meses

if pres > exceder:
    print('O financiamento foi negado!')
else:
    print('Financiamento aprovado, Parabéns!')