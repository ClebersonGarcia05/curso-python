'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

for i in range(5):
    peso = float(input(f'Digite o {i+1}º peso: '))
    if i == 0:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        elif peso < me:
            me = peso
print(ma)
print(me)