""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag). """

soma = 0
cont = 0
while True:
    num = int(input('Digite um valor [999 para parar o programa]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A quantidade de valores digitados foi {cont} números e a soma entre eles é {soma}')