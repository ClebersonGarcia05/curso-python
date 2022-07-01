""" Adicione ao modulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas 
informações, geradas pelas funções que já temos no módulo criado até aqui. """

from utilidadesCev.moeda import moeda

num = float(input('Digite um valor: '))
porc = int(input('Digite qual a porcentagem: '))

moeda.resumo(num, porc)