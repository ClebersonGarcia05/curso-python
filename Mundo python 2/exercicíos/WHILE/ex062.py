""" Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos"""

pt = int(input('Digite o primeiro termo: '))
r = int (input('Digite a razão: '))
cont = 10
t = 0
while cont != 0:
    t += 1
    print(pt, end=' → ')
    pt += r
    cont -= 1
    if cont == 0:
        print('Pausa\n\nQuer mostrar mais termos?\n ')
        cont = int(input('Mais quantos termos?'))
print('\nPrograma finalizado')
print(f'Total de termos mostrados: {t}')