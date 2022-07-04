""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

Á vista dinheiro/cheque: 10% de desconto
Á vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros"""

preco = float(input('Qual o valor do produto: '))

print('Qual a forma de pagamento?')
print(""" \n1 - A vista com dinheiro ou cheque\n
2 - A vista com cartão\n
3 - Em 2x no cartão\n
4 - 3x ou mais no cartão """)
pag = int(input('\nDigite a oção desejada:'))

if pag == 1:
    print(f'\nVocê recebeu 10% de desconto, o valor do produto com desconto é: R${preco - (preco * 10 / 100)}')
elif pag == 2:
    print(f'\nVocê recebeu 5% de desconto, o valor do produto com desconto é: R${preco - (preco * 5 / 100)}')
elif pag == 3:
    print(f'\nO valor do produto é: R${preco} \nE o valor de cada parcela é: R${preco / 2}')
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'O valor das parcelas será de {parcelas}x de {(preco + (preco * 20 / 100)) / parcelas}')
    print(f'\nDevido ao parcelamento o valor teve um reajuste em 20%, o valor com juros é de: R${preco + (preco * 20 / 100)} no total')
else:
    print('Opção Inválida, tente novamente!')