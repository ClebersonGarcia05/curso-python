""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia. No final 
mostre uma listagem de preços, organizando os dados em forma tabula. """

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
prod = ('Lapis', 1.75, 'Caderno', 15, 'Caneta', 2)
for i in range(0, len(prod)):
    if i %2 == 0:
        print(f'{prod[i]:.<30}', end='')
    else:
        print(f'R${prod[i]:>7.2f}')
print('-'*40)