""" Refaça o exercicio 035 dos triangulos, acrescentando o resurso de mostrar que tipo de triangulo será formado:

Equilátero: todos os lados iguais

Isóceles: dois lados iguais

Escaleno: Todos os lados diferentes """

seg1 = float(input('Digite o primeiro seguimento: '))
seg2 = float(input('Digite o segundo seguimento: '))
seg3 = float(input('Digite o terceiro seguimento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 and seg1 == seg3:
        print('\033[34mEsses seguimentos formam um triangulo equilátero\033[m')
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print('\033[32mEses seguimentos formam um triangulo isóceles\033[m')
    else:
        print('\033[35mEses seguimentos formam um triangulo escaleno\033[m')
else:
    print('\033[31mEsses valores não podem formar um triangulo!\033[m')