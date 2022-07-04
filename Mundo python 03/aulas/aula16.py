""" Tuplas são criadas com parenteses e tuplas são imutáveis (Não podem ser alteradas)

Ex: lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') 

enumerate = numera a posição de cada item
sorted = coloca os itens de forma organizada (A - Z), mas não altera a tupla
index = posição de onde está o número ou letra.
del = apaga tudo
uma tupla + outra tupla são juntadas.

Ex: a = (2,5,8)
b = (5,9,7,4)
c = a + b
a saida vai ser (2,5,8,5,9,7,4)"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
""" for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
 """
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')