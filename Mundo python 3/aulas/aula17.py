""" .append() - Adiciona um valor no final de uma lista 
    .insert(posição, valor) - Adiciona um valor em uma posição existente da lista que você escolher
    del lista[posição] - Elimina a posição escolhida
    .pop(posição) - Geralmente é para eliminar o último valor da lista, porém pode ser passado a posição como parametro
    .remove(valor) - Elimina o valor escolhido
    .sort() - Coloca os valores em ordem crescente
    .sort(reverse=True) - Coloca os valores em ordem decrescente"""


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.append(10)
lista.insert(0, 'olá')
del lista[0]
lista.pop()
lista.pop(2)
lista.sort(reverse=True)
lista.remove(0)
print(lista)

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    if 999 in valores:
        break
print(valores)