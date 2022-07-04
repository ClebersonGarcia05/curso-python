""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
conter apenas os valores pares e os valores impares digitados, respectivamente. No final mostre o conteúdo das três 
listas geradas. """

num = []
par = []
imp = []

while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Opção inválida, deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
for v in num:
    if v %2 == 0:
        par.append(v)
    else:
        imp.append(v)
num.sort()
par.sort()
imp.sort()
print(num)
print(par)
print(imp)