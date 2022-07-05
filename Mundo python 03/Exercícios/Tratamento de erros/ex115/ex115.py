""" Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto 
simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas. """

from time import sleep
from lib.interface import cabecalho, menu, leiaInt
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    r = menu(['Cadastrar nova pessoa', 'Listar pessoas', 'Sair do sistema'])
    if r == 1:
        cabecalho('Novo cadastro')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
    elif r == 2:
        cabecalho('Listar pessoas cadastradas')
        lerArquivo(arq)
    elif r == 3:
        cabecalho('Saindo do sistema...até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)