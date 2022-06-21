""" Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha. """

lista = [[],[],[]]
s = 0
stc = 0
for i in range(3):
    for j in range(3):
        lista[i].append(int(input(f'Digite um valor [{i}][{j}]: ')))
print('\nA matriz dos números digitados é: ')
for pos, i in enumerate(lista):
    for p, v in enumerate(lista[pos]):
        if p == 2:
            stc += v
        if v %2 == 0:
            s += v
        print(v, end=' ')
    print()
ma = max(lista[1])
print(f'O maior valor da 2º linha é: {ma}')
print(f'A soma entre os valores pares é: {s}')
print(f'A soma dos valores da terceira coluna é: {stc}')