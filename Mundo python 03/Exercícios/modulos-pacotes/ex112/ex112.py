""" Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107,108 e 109 para o primeiro pacote e mantenha tudo funcionando """

from utilidadesCev import moeda, dado

num = dado.leiaDinheiro('Digite um preço: R$')
moeda.resumo(num, 15)