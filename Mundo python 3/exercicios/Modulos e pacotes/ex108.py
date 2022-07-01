""" Adapte o código do desafio 107, criando uma função adcional chamada, moeda(), que consiga mostrar os valores como um 
valor monetário formatado. """

from utilidadesCev.moeda import moeda

num = float(input('Digite um valor: '))
porc = int(input('Digite qual a porcentagem: '))

print(f'{moeda.moeda(num)} com {porc}% de aumento é: {moeda.moeda(moeda.aumentar(num, porc))}')
print(f'{moeda.moeda(num)} com {porc}% de desconto é: {moeda.moeda(moeda.diminuir(num, porc))}')
print(f'O dobro de {moeda.moeda(num)} é: {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é: {moeda.moeda(moeda.metade(num))}')