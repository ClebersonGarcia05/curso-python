""" Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno """

def area(c, l):
    print(f'A área do comprimento {c} e largura {l} é: {c * l}m²')

c = float(input('Qual o comprimento? '))
l = float(input('Qual a largura? '))
area(c, l)