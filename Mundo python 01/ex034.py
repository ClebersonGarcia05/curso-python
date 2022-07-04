salario = float(input('Informe o salário do funcionário: '))

aum = 0
if salario >= 1250.00:
    aum = salario * (10/100)
    print(f'Esse funcionário teve um aumento de R${aum:.2f}, o salário com o aumento é de: R${salario + aum:.2f}')
else:
    aum = salario * (15/100)
    print(f'Esse funcionário teve um aumento de R${aum:.2f}, o salário com o aumento é de: R${salario + aum:.2f}')