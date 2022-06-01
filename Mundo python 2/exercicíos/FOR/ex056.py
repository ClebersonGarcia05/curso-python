'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:

A média de idade do grupo

Qual é o nome do homem mais velho

Quantas mulheres tem menos de 20 anos'''
ma = 0
cont = 0
soma = 0
for i in range(4):
    nome = str(input(f'Digite o nome da {i+1}º pessoa: ')).strip().capitalize()
    idade = int(input(f'Digite a idade da {i+1}º pessoa: '))
    sexo = str(input(f'Sexo [M/F] ')).strip().lower()
    soma += idade
    if sexo != 'm' or sexo != 'f':
        print('Opção inválida, tente novamente!')
        break
    elif sexo == 'f' and idade < 20:
        cont += 1
    elif i == 0:
        ma = idade
    elif idade > ma:
        ma = idade
        if sexo == 'm':
            n = nome
if sexo != 'm' or sexo != 'f':
    exit()
media = soma / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {ma} anos e se chama {n}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')

#OU

""" cont = 0
media = 0
for i in range(4):
    nome = str(input(f'Digite o nome da {i+1}º pessoa: '))
    idade = int(input(f'Digite a idade da {i+1}º pessoa: '))
    print('''    
    [1] Masculino
    [2] Feminino''')
    sexo = int(input('Digite a opção para o sexo da pessoa: '))
    media += idade
    if sexo < 1 or sexo > 2:
        print('Opção não existe, tente novamente!')
        break
    elif sexo == 2 and idade < 20:
        cont +=1
    elif i == 0:
        ma = idade
    elif idade > ma:
        ma = idade
        if sexo == 1:
            n = nome
if sexo <1 or sexo > 2:
    exit()
print(f'Nome do homem mais velho é {n} com a idade de {ma} anos')
print(f'A quantidade de mulheres abaixo de 20 anos é: {cont}')
print(f'A média de idade do grupo é: {media / 4}') """