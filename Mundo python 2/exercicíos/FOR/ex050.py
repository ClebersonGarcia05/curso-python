'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o'''
s = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        s += num
        cont += 1

print(f'Você informou {cont} numeros pares e a soma dos número é: {s}')