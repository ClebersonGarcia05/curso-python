'''Faça um programa que leia um valor de produto

Tenho o dinheiro para pagar a vista, mas quero parcelar em 10x sem juros

O dinheiro guardado me renderá 1% ao mês'''

val = float(input('Qual o valor do produto?'))
parc = int(input('Quantas vezes você quer parcelar?'))
juros = float(input('Qual a porcentagem de juros no ano? '))

juros = juros / 12
totalParcela = val / parc

print(f'O valor vai ficar em {parc}x de {totalParcela:.2f} ')

for i in range(parc+1):
    nu = val + (val * juros / 100)
    val = nu
    print(f'{val:.2f}')
    if val >= 0:
        val -= totalParcela
    else:
        break

print(f'\nEm {parc} meses seu dinheiro vai render {nu:.2f} de juros')