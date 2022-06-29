""" Faça um programa que tenha uma lista chamada números e duas funções sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteador pela função anterior. """

from random import sample
def somaPar(lista):
    soma = 0
    for i in lista:
        if i %2 == 0:
            soma += i
    print(f'A soma entre os valores pares é: {soma}')
def sorteia(lista):
    lista = sample(lista, 5)
    print(f'Os números sorteado foram: {lista}')
    somaPar(lista)

#Programa Principal
num = []
while True:
    n = int(input('Adicione números [0 para parar]: '))
    if n == 0:
        break
    num.append(n)
sorteia(num)