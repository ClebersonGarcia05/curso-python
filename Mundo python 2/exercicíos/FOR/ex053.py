'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços'''

#Transforma os caracteres em minusculo com (lower()) e tira os espaços em branco do começo e final com (strip())
frase = str(input('Digite uma frase: ')).lower().strip() 

#Separa as palavras com base nos espaços entre elas com (split())
palavras = frase.split()
#Junta todas as palavras sem nada para separa-las com ('entre as aspas vai o que você quer que separa elas, ou vazio para não separar'.join())
junto = ''.join(palavras)
inverso = junto[::-1]

#OU frase.replace(" ", "") para subistituir os espaços por nada. 
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('E temos um palindromo')
else:
    print('Não é palindroma')

#OU

""" for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palindromo!') """
