""" Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta """

lista = [[],[],[]]
for i in range(3):
    for j in range(3):
        lista[i].append(int(input(f'Digite um valor [{i}][{j}]: ')))
print('\nA matriz dos números digitados é: ')
for pos, i in enumerate(lista):
    for v in lista[pos]:
        print(v, end=' ')
    print()