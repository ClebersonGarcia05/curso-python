""" Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de 
colocação. Depois mostre: 

A) Apenas os 5 primeiros colocados. 

B) Os últimos 4 colocados na tabela. 

C) Uma lista com os times em ordem alfabética. 

D) Em que posição na tabela está o time da chapecoense. """

times = ('Flamengo', 'Palmeiras', 'Atlético', 'Grêmio', 'Athletico', 'Santos', 'São Paulo', 'Internacional', 
'Fluminense', 'Corinthians', 'Fortaleza', 'Bahia', 'Ceará', 'Cruzeiro', 'América', 'Atlético', 'Chapecoense', 'Botafogo', 
'Vasco da Gama', 'RB Bragantino')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'Posição do time Chapecoense: {times.index("Chapecoense")+1}º')