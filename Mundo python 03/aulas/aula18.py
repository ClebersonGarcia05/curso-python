""" lista.apeend(lista2[:]) = O nome da lista com o símbolo [:] forma uma cópia da lista
lista[0][0] = o primeiro indice acessa a primeira lista e o segundo indice acessa a segunda lista"""

pessoas = []
dados = ['Cleberson', 22, 'M']

dados.append('Alessandra')
pessoas.append(dados[:])

print(pessoas[0][0])