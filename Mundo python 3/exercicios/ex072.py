""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até vinte. Seu programa
deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso. """

extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Número inválido, digite um número entre 0 e 20: '))
    print(f'O número digitado por extenso é: {extensos[num]}')