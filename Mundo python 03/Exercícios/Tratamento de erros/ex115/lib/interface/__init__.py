def leiaInt(msg):
    while True:
        try:
            num = int(input(f'{msg}'))
        except ValueError:
            print('\033[31mERRO! Valor incorreto, tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os valores!\033[m')
            return 0
        else:
            return num

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.upper().center(42))
    print(linha())

def menu(lista):
    cabecalho('menu principal')
    for c, v in enumerate(lista):
        print(f'\033[33m{c+1}\033[m - \033[34m{v}\033[m')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
