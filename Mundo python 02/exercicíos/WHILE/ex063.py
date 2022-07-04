""" Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequencia de Fibonacci 

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8"""

termos = int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end='')
while cont < termos:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' → Fim')