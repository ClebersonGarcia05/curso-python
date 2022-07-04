""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
De 25 até 30: Sobrepeso
De 30 até 40: Obesidade
Acima de 40:Obesidade mórbida """

alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (alt * alt)

print(f'O IMC dessa pessoa é {imc:.1f}')

if imc <= 18.5:
    print('Você está abaixo do peso! \033[33mCuidado!\033[m')
elif imc <= 25:
    print('Você está com o peso ideal! \033[32mParabéns!\033[m')
elif imc <= 30:
    print('Você está com sobrepeso! \033[33mCuidado!\033[m')
elif imc <= 40:
    print('Você está com obesidade! \033[33mProcure uma nutricionista\033[m')
else:
    print('Você está com obesidade mórbida! \033[31mProcure um médico urgente!\033[m')