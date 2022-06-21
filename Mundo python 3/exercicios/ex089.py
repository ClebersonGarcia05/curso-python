""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente. """

lista = [[], [], [], []]
while True:
    lista[0].append(str(input('Digite o nome do aluno: ')).capitalize().strip())
    lista[1].append(float(input('Digite a primeira nota: ')))
    lista[2].append(float(input('Digite a segunda nota: ')))

    r = str(input('Deseja continuar cadastrando? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Opção inválida, deseja continuar cadastrando? [S/N]')).upper().strip()[0]
    if r == 'N':
        break
print(f'\n{"NOME":<12} {"MÉDIA":^12}')
for pos, v in enumerate(lista[0]):
    lista[3].append((lista[1][pos] + lista[2][pos]) / 2)
    print(f'{v:<12} {lista[3][pos]:^12}')
nome = str(input('\nDeseja visualizar as notas de qual aluno? [0 para sair]: ')).capitalize().strip()
if nome == 0:
    exit()
print(f'{"NOME":<12} {"NOTA 1":^12} {"NOTA 2":^12}')
for pos, v in enumerate(lista[0]):
    if v == nome:
        print(f'{v:<12} {lista[1][pos]:^12} {lista[2][pos]:^12}')