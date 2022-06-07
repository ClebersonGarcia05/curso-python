""" Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário qual será o 
valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere 
que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""

while True:
    valor = int(input('Digite o valor a ser sacado: '))
    cin = valor // 50
    print(f'Quantidade de {cin} de R$50,00')
    valor = valor - (cin * 50)
    vin = valor // 20
    print(f'Quantidade de {vin} de R$20,00')
    valor = valor - (vin * 20)
    dez = valor // 10
    print(f'Quantidade de {dez} de R$10,00')
    valor = valor - (dez * 10)
    um = valor
    print(f'Quantidade de {um} de R$1,00')