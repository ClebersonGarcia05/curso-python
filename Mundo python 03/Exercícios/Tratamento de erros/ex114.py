""" Crie um código em Python que teste se o site Pudim está acessível pelo computador usado. """

from time import sleep
import urllib
import urllib.request

site = str(input('Insira o site: www.'))
try:
    site1=urllib.request.urlopen(f'http://www.{site}/')
except urllib.request.URLError:
    print('Acessando o site...')
    sleep(2)
    print(f'\033[31mO site www.{site} não está acessível no momento.\033[m')
else:
    print('Acessando o site...')
    sleep(2)
    print(f'\033[32mConsegui acessar o site www.{site} com sucesso!\033[m')