""" Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores. """


from time import sleep

def ajuda(c):
    titulo(f'Acessando o manual do comando \'{c}\'')
    help(c)
    sleep(2)

def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}  ')
    print('-' * tam)
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE COMANDO PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')