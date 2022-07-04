""" Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela. """

aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Digite a média: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(f'O aluno {aluno["nome"]} teve a média {aluno["media"]} e sua situação é {aluno["situação"]}.')
print(aluno)