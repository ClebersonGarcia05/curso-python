km = float(input('Digite quantos quilometros tem a viagem: '))

if km <= 200:
    print(f'O valor da passagem é de: R${0.50 * km:.2f}')
else:
    print(f'O valor da passagem é de: R${0.45 * km:.2f} ')