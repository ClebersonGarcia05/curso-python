""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.

B) A lista de valores ordenada de forma decrescente

C) Se o valor 5 foi digitado e está ou não na lista."""

num = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Resposta inválida, deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
num.sort(reverse=True)
print(f'A lista em forma decrescente é: {num}')
if 5 in num:
    print(f'O valor 5 foi digitado {num.count(5)} vezes')
else:
    print(f'O valor 5 não foi encontrado na lista.')
print(f'Foi digitado {len(num)} números.')