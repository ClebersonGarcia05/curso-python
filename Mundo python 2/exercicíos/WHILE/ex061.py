""" Refaça o desafio 051, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos da
progressão usando a estrutura while """

pt = int(input('Digite o primeiro termo: '))
r = int (input('Digite a razão: '))
cont = 10
while cont != 0:
    if cont == 10:
        print(pt, end=' → ')
        cont -= 1
    cont -= 1
    pt += r
    print(pt, end=' → ')
print('Acabou')