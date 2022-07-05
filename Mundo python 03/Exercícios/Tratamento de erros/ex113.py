""" Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de
um número de tipo inváldo. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. """

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[31mERRO! Valor incorreto, tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os valores!\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg).replace(',', '.'))
        except ValueError:
            print('\033[31mERRO! Valor incorreto, tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os valores!\033[m')
            return 0
        else:
            return num


numint = leiaInt('Digite um valor inteiro: ')
numfloat = leiaFloat('Digite um valor real: ')

print(f'O número inteiro digitado foi {numint} e o número real digitado foi {numfloat}')