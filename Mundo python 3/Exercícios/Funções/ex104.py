""" Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python, só 
que fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaint('Digite um número: ') """

def leiaInt():
    while True:
        num = str(input('Digite um número: '))
        if num.isnumeric():
            print(f'Você acabou de digitar o número {num}')
            break
        else:
            print('\033[31mIsso não é um número!\033[m')
leiaInt()