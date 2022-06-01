'''Aula de laços de repetição (for)'''

'''
for c in range(1, 10) conta de 1 a 9
for c in range(1, 11) conta de 1 a 10
for c in range(10, 0, -1) conta de 10 a 1 conta para trás de 1 em 1
for c in range(10, 0, -2) conta de 10 a 1 conta para trás de 2 em 2 etc...
'''
n = int(input('Digite um valor: '))
print(f'Tabuada do {n}\n')
for i in range(1, 11):
    print(f'{n} x {i} = {n*(i)}')