from random import choice

pri = str(input('Qual o nome do 1º aluno: '))
seg = str(input('Qual o nome do 2º aluno: '))
ter = str(input('Qual o nome do 3º aluno: '))
quar = str(input('Qual o nome do 4º aluno: '))

lista = [pri, seg, ter, quar]
escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido}')