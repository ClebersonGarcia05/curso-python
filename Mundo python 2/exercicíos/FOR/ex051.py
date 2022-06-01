'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos desssa progressão'''

pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
dec = pa + (11 -1) * r

print(f'\nA progração aritimética com começo no termo {pa} e com a razão {r} é:')
for i in range(pa, dec, r):
    print(f'{i}', end=" → ")
print('FIM\n')
#OU
""" 
for i in range(10):
    print(pa)
    pa += r """