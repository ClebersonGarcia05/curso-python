""" Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o 
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108. """

import moeda

num = float(input('Digite um valor: '))
porc = int(input('Digite qual a porcentagem: '))

print(f'{moeda.moeda(num, mostrar=False)} com {porc}% de aumento é: {moeda.aumentar(num, porc, mostrar=False)}')
print(f'{moeda.moeda(num)} com {porc}% de desconto é: {moeda.diminuir(num, porc)}')
print(f'O dobro de {moeda.moeda(num)} é: {moeda.dobro(num)}')
print(f'A metade de {moeda.moeda(num)} é: {moeda.metade(num)}')