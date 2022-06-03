""" Faça um programa que leia um número e mostre o seu fatorial
EX: 5! = 5x4x3x2x1 = 120 """

from math import factorial

num = int(input('Digite um número para saber o fatorial: '))
print(f'Calculando {num}! = ', end='')
c = num
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

#OU
""" 
arm = 1
fat = 1
num = int(input('Digite um número para saber o fatorial: '))
esc = num
while arm > 0:
    arm = num
    fat *= num
    arm -= 1
    num -= 1
print(f'O fatorial do número {esc} é: {fat}') """

#OU
""" 
num = int(input('Digite um número para saber o fatorial: '))
f = factorial(num)
print(f'O fatorial do número {num} é: {f}') """

""" for i in range(num, -1, -1):
    if i > 0:
        soma *= i
print(soma) """