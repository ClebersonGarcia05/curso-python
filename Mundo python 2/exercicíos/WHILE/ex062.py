""" Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encessa quando ele disser que quer mostrar 0 termos"""

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
    if cont == 0:
        print('Acabou\nQuer mostrar mais termos? ')
        n = int(input('Digite 1 para sim ou 0 para não: '))
        if n == 1:
            pt += r
            cont = 10
        elif n < 0 or n > 1:
            print('Opção inválida, tente novamente!')
        else:
            cont = 0
print('Programa finalizado')