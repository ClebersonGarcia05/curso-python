""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão 

1 para binário
2 para octal
3 para hexadecimal"""

num = int(input('Digite um número: '))

print('\nDigite 1 para saber a forma binária')
print('\nDigite 2 para saber a forma octal')
print('\nDigite 3 para saber a forma hexadecimal')

res = int(input('\nDigite a oção: '))

if res == 1:
    print(f'\nA forma binária de {num} é {format(num, "b")}') # ou bin(num)[2:]
elif res == 2:
    print(f'\nA forma octal de {num} é {format(num, "o")}') # ou oct(num)[2:]
elif res == 3:
    print(f'\nA forma hexadecimal de {num} é {format(num, "x")}') # ou hex(num)[2:]
else:
    print('\nOpção invalida! tente novamente!')