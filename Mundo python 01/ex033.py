n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

ma = 0
me = 0
if n1 > n2 and n1 > n3:
    ma = n1
if n1 < n2 and n1 < n3:
    me = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n2 < n1 and n2 < n3:
    me = n2
if n3 > n1 and n3 > n2:
    ma = n3
else:
    me = n3

print(f'O maior número é: {ma}')
print(f'O menor número é: {me}')