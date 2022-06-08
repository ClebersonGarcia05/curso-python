""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 

A) Quantas vezes apareceu o valor 9. 

B)Em que posição foi digitado o primeiro valor 3. 

C) Quais foram os números pares. """

num = (int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:')),
        int(input('Digite um número:')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os números pares são: ', end='')
for n in num:
    if n%2 == 0:
        print(n, end=' ')

#Difícil        
""" var = cont = 0
n = -1
while True:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite um valor: '))
    n3 = int(input('Digite um valor: '))
    n4 = int(input('Digite um valor: '))
    valores = (n1, n2, n3, n4)
    print(f'Os números pares são: ', end='')
    for i in range(len(valores)):
        if valores[i] == 3:
            var = i+1
        if valores[i] == 9:
            cont += 1
        if valores[i] %2 == 0:
            n = valores[i]
            print(n, end=' ')
    break
print(f'\nO número 9 apareceu {cont} vezes')
if var > 0:
    print(f'O número 3 apareceu na {var}º posição.') """