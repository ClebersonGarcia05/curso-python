from random import shuffle as su

n1 = str(input('Qual o nome do 1º aluno: '))
n2 = str(input('Qual o nome do 2º aluno: '))
n3 = str(input('Qual o nome do 3º aluno: '))
n4 = str(input('Qual o nome do 4º aluno: '))

lista = [n1, n2, n3, n4]
su(lista)

print(f'A ordem de apresentação do trabalho é: {lista}')