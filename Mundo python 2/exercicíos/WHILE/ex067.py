""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    num = int(input('\nDigite um número: '))
    if num < 0:
        break
    print(f'='*25)
    print(f'A tabuada do número {num} é: ')
    print(f'='*25)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
print(f'Programa finalizado com sucesso. Volte sempre!')