""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 

A) Quantas vezes apareceu o valor 9. 

B)Em que posição foi digitado o primeiro valor 3. 

C) Quais foram os números pares. """

cont = 0

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = str(input('Digite um valor: '))
valores = (n1, n2, n3, n4)

posi = 0
for i in range(0, len(valores)):
    if valores[i] == 9:
        cont += 1
    if valores[i] == 3:
        posi = i
print(f'O número 9 apareceu {cont} vezes')
print(f'{posi}')