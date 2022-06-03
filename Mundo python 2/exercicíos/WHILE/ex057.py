""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto. """

sexo = str(input('Sexo [M/F]: ')).upper().strip()
while sexo not in 'MF':
    print('Opção invalida, tente novamente!\n')
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso!\n')
#OU
""" 
if sexo == 'M' or sexo == 'F':
        print('Opção VALIDA! Siga.')
while sexo != 'M' and sexo != 'F':
    print('Opção invalida, tente novamente!\n')
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        print('Opção VALIDA! Siga.') """