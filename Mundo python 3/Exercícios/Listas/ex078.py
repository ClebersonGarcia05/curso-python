""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e menor valor digitado e as suas respectivas posições na lista """

ma = me = 0
valores = []
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    #print('Valor adicionado com sucesso...')
print(f'\nVocê digitou os valores: {valores}')
print(f'O maior valor é {max(valores)} e as posições são: ', end='')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos}', end='...')
print(f'\nO menor valor é {min(valores)} e as posições são: ', end='')
for pos, v in enumerate(valores):
    if v == min(valores):
        print(f'{pos}', end='...')