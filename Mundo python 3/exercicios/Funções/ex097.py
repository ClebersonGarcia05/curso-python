""" Faça um programa que tenha uma função chamada escreva() , que receba um texto qualquer como parâmetro e mostre uma 
mensagem com tamanho adptável.

EX:
escreva('Olá mundo!')

Saída:
----------
Olá mundo!
----------"""

def escreva(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))

escreva('Olá, mundo!')
escreva('Bem vindo ao mundo da programação!')
escreva('Python é a melhor linguagem para se aprender a programar!')