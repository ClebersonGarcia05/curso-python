""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. """

jog = {}
gols = []
nome = str(input('Digite o nome do jogador: '))
part = int(input(f'Digite quantas partidas o {nome} jogou: '))
jog['Nome'] = nome
for i in range(part):
    gols.append(int(input(f'Quantidade de gols feitos na {i+1}º partida: ')))
jog['gols'] = gols.copy()
jog['total'] = sum(gols)
print('-=' * 30)
print(jog)
print('-=' * 30)
for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jog["Nome"]} jogou {part} partidas.')
for i, v in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jog["total"]} gols')