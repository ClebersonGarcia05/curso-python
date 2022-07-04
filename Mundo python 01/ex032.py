from datetime import date

ano = int(input('Coleque um ano para analisar ou para analisar o ano atual digite 0: '))

print('Analisando...')

if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é um ano bissexto!')
else:
    print(f'O ano de {ano} não é um ano bissexto!')