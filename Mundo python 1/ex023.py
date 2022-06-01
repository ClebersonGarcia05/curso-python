num = int(input('Digite um número entre 0 e 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f'A casa de unidade é: {uni} ')
print(f'A casa de dezena é: {dez}')
print(f'A casa de centena  é: {cen}')
print(f'A casa de milhar é: {mil}')