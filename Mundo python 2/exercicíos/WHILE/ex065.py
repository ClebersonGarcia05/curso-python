""" Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não 
continuar a digitar valores """

cont = 0
num = 1
soma = 0
maior, menor = 0, 0
while num > 0:
    num = int(input('Digite um número: '))
    esc = str(input('Deseja continuar digitando valores? [S/N]: ')).upper().strip()
    soma += num
    cont += 1
    if num == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    elif esc == 'S':
        pass
    elif esc != 'N' and esc != 'S':
        print('Opção invalidade, tente novamente!')
        num = 1
    else:
        num = 0
media = soma / cont
print(f'A soma dos valores é {soma} e a média dos valores digitados é {media}')
print(f'O maior número digitado é: {maior} e o menor número digitado é: {menor}')