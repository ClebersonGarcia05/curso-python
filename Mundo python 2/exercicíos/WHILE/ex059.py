""" Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa 

Seu programa deverá realizar a operação em cada caso"""
from time import sleep

#Define um valor padrão para as variaveis soma, esc e prod
soma = 0
esc = 0
prod = 1
#Enquanto a esc for diferente de 5 o programa não sai do loop
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite um valor: '))
while esc != 5:
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa """)
    esc = int(input('Digite a opção desejada: '))
    if esc == 1:
        soma = num1 + num2
        print(f'O valor da soma entre {num1} e {num2} é: {soma}')
    elif esc == 2:
        prod = num1 * num2
        print(f'O produto dos valores {num1} e {num2} é: {prod}')
    elif esc == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que o número {num2}')
        else:
            print(f'O número {num2} é maior que o número {num1}')
    elif esc == 4:
        num1 = float(input('Digite um valor: '))
        num2 = float(input('Digite um valor: '))
    elif esc > 5 or esc < 1:
        print('Opção inválida, tente novamente')
        esc = 0
    else:
        print('Encerrando programa...')
        sleep(2)
        print('Aguarde...')
        sleep(2)
        print('Programa finalizado com sucesso!')
    sleep(1)