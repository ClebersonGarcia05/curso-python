nome = str(input('Qual o seu nome?')).strip().capitalize()

if nome == 'Cleberson':
    print(f'Que nome bonito você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Que belo nome!')
else:
    print(f'Seu nome é bem normal')

print(f'Tenha um bom dia, {nome}!')