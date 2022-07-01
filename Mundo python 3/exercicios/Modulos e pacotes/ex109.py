""" Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o 
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108. """

from utilidadesCev.moeda import moeda

num = float(input('Digite um valor: '))
porc = int(input('Digite qual a porcentagem: '))

print(f'{moeda.moeda(num, mostrar="True")} com {porc}% de aumento é: {moeda.moeda(moeda.aumentar(num, porc), mostrar="False")}')
print(f'{moeda.moeda(num, mostrar="True")} com {porc}% de desconto é: {moeda.moeda(moeda.diminuir(num, porc), mostrar="True")}')
print(f'O dobro de {moeda.moeda(num, mostrar="True")} é: {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num, mostrar="True")} é: {moeda.moeda(moeda.metade(num))}')