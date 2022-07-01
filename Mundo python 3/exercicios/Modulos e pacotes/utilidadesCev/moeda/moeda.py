def aumentar(num, porc, mostrar=False):
    num = num + (num * porc / 100)
    if mostrar == True:
        return moeda(num)
    else:
        return num


def diminuir(num, porc, mostrar=False):
    num = num - (num * porc / 100)
    if mostrar == True:
        return moeda(num)
    else:
        return num


def dobro(num, mostrar=False):
    num = num * 2
    if mostrar == True:
        return moeda(num)
    else:
        return num


def metade(num, mostrar=False):
    num = num / 2
    if mostrar == True:
        return moeda(num)
    else:
        return num


def moeda(num, mostrar=True):
    if mostrar == True:
        return f'R${num:.2f}'
    else:
        return num


def resumo(num, porc):
    msg = 'RESUMO DE VALOR'
    tam = len(msg) + 15
    print('-' * tam)
    print(f'{"RESUMO DE VALOR":>15}')
    print('-' * tam)
    print(f'{"Preço analisado:":<20} {moeda(num)}')
    print(f'{"Dobro do preço:":<20} {dobro(num, True)}')
    print(f'{"Metade do preço:":<20} {metade(num, True)}')
    print(f'{f"{porc}% de aumento:":<20} {aumentar(num, porc, True)}')
    print(f'{f"{porc}% de desconto:":<20} {diminuir(num, porc, True)}')
    print('-' * tam)
