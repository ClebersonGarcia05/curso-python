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


