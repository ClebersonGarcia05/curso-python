print('-=' * 20)
seg1 = float(input('Digite o primeiro seguimento: '))
print('-=' * 20)
seg2 = float(input('Digite o segundo seguimento: '))
print('-=' * 20)
seg3 = float(input('Digite o terceiro seguimento: '))
print('-=' * 20)

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print(f'É possível formar um triangulo com esses seguimentos!')
else:
    print('Esses seguimentos NÂO podem formar um triangulo!')