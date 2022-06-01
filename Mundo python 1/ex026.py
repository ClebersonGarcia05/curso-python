frase = str(input('Digite a frase: ')).strip()

contador = frase.lower().count('a')
primeira = frase.lower().find('a')
ultima = frase.lower().rfind('a')
print(f'A letra A aparece {contador} vezes!')
print(f'A posição da primeira letra A apareceu na posição: {primeira + 1}')
print(f'A posição da última letra A aparece na posição: {ultima + 1}')