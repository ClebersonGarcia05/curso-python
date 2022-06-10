""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibido todos os valores únicos
digitados em ordem crescente """

val = []
while True:
    n = int(input('Digite um valor: '))
    if n not in val:
        val.append(n)
        print('Número cadastrado com sucesso')
    else:
        print('O número já está cadastrado, não vou adicionar!')
    resp = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('\nOpção Invalida, quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
val.sort()
print(f'Você digitou os valores: {val}')