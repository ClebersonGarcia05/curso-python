""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente. """

lista = [[], [], [], []]
while True:
    lista[0].append(str(input('Digite o nome do aluno: ')))
    lista[1].append(float(input('Digite a primeira nota: ')))
    lista[2].append(float(input('Digite a segunda nota: ')))

    r = str(input('Deseja continuar cadastrando? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Opção inválida, deseja continuar cadastrando? [S/N]')).upper().strip()[0]
    if r == 'N':
        break
for pos, v in enumerate(lista[0]):
    for i in lista[1]:
        print(i)
        for j in lista[2]:
            print(j)
            lista[3].append((i + j) / 2)
    print(f'O aluno {v} teve a média {lista[3][pos]}')