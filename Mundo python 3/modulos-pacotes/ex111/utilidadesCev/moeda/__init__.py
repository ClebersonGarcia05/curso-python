def aumentar(num, porc, mostrar=True):
    num = num + (num * porc / 100)
    return moeda(num) if mostrar is True else num


def diminuir(num, porc, mostrar=True):
    num = num - (num * porc / 100)
    return moeda(num) if mostrar is True else num


def dobro(num, mostrar=True):
    num = num * 2
    return moeda(num) if mostrar is True else num


def metade(num, mostrar=True):
    num = num / 2
    return moeda(num) if mostrar is True else num


def moeda(num, mostrar=True):
    if mostrar == True:
        return f'R${num:.2f}'.replace('.', ',')
    else:
        return num


def resumo(num, porc):
    print('-' * 30)
    print(f'{"RESUMO DE VALOR".center(30)}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num)}')
    print(f'Metade do preço: \t{metade(num)}')
    print(f'{porc}% de aumento: \t{aumentar(num, porc)}')
    print(f'{porc}% de desconto: \t{diminuir(num, porc)}')
    print('-' * 30)
