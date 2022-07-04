""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

Média abaixo de 5.0: Reprovado 
Média entre de 5.0 e 6.9: Recuperação 
Média 7.0 ou superior: Aprovado """

n1 = float(input('Digite qual a nota 1: '))
n2 = float(input('Digite qual a nota 2: '))

m = (n1 + n2) / 2

if m < 5:
    print(f'Sua média foi {m} e você foi Reprovado!\nEstude mais!')
elif m >= 5 and m <= 6.9:
    print(f'Sua média foi {m} e você terá que ficar de Recuperação!')
else:
    print(f'Sua média foi de {m} e você foi Aprovado, parabéns!')