""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de 
números gerados e também indique o menor e o maior valor que estão na tupla. """

from random import randint

me = ma = 0
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for i in range (0, len(num)):
    if i == 0:
        me = num[i]
        ma = num[i]
    elif num[i] < me:
        me = num[i]
    elif num[i] > ma:
        ma = num[i]
print(f'A tupla de números é: {num}')
print(f'O maior número da tupla é: {ma}')
print(f'O menor número da tupla é: {me}')
print(f'O menor número da tupla é: {min(num)}')
print(f'O maior número da tupla é: {max(num)}')