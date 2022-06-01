""" Escreva um programa que leia dois números interiros e caompare-os, mostrando na uma mensagem:

O primeiro valor é maior

o segundo valor é maior

Não existe valor maior, os dois são iguais """


n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 == n1:
    print('Não existe valor maior, os dois são iguais!')
else:
    print('O segundo valor é maior!')