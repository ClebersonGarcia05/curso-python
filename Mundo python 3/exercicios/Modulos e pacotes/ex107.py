""" Crie um módulo chamado moeda.py que tenhas as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.  """

from utilidadesCev.moeda import moeda

num = float(input('Digite um valor: '))
porc = int(input('Digite qual a porcentagem: '))

print(f'O valor {num} com {porc}% de aumento é: {moeda.aumentar(num, porc)}')
print(f'O valor {num} com {porc}% de desconto é: {moeda.diminuir(num, porc)}')
print(f'O dobro de {num} é: {moeda.dobro(num)}')
print(f'A metade de {num} é: {moeda.metade(num)}')