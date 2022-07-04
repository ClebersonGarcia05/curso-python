def aumentar(num, porc, mostrar=False):
    return num + (num * porc / 100)


def diminuir(num, porc, mostrar=False):
    return num - (num * porc / 100)


def dobro(num, mostrar=False):
    return num * 2


def metade(num, mostrar=False):
    return num / 2


def moeda(num):
    return f'R${num:>.2f}'.replace('.', ',')