'''Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

num = int(input('Digite um número: '))

print(f'A tabuada do número {num} é: ')

for i in range(1, 11):
    print(f'{num} x {i} = {i * num}')