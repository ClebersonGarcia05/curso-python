nome = str(input('Qual o seu nome completo?')).strip()

separar = nome.split()

print(f'O seu primeiro nome é: {separar[0]}')
print(f'O seu ultimo nome é: {separar[len(separar) - 1]}')